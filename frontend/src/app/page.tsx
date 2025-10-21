'use client'
import React, { useEffect, useState, useMemo } from 'react'
import dynamic from 'next/dynamic'

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000'
const ECharts = dynamic(() => import('echarts-for-react'), { ssr: false })

export default function Page() {
  const [tab, setTab] = useState('introducao')
  const [students, setStudents] = useState<any[]>([])
  const [filtered, setFiltered] = useState<any[]>([])
  const [search, setSearch] = useState('')
  const [gender, setGender] = useState('all')
  const [selectedStudent, setSelectedStudent] = useState<any>(null)
  const [prediction, setPrediction] = useState<any>(null)
  const [predictLoading, setPredictLoading] = useState(false)

  useEffect(() => { fetchStudents() }, [])

  async function fetchStudents() {
    try {
      const res = await fetch(`${API_BASE}/students`)
      if (!res.ok) throw new Error('Erro ao buscar alunos')
      const data = await res.json()
      setStudents(data)
      setFiltered(data)
    } catch (err) {
      const mock = [
        { id: 1, name: 'Aluno A', gender: 'M', age: 15, faltas: 12, nota_final: 6.2 },
        { id: 2, name: 'Aluno B', gender: 'F', age: 17, faltas: 4, nota_final: 8.5 },
        { id: 3, name: 'Aluno C', gender: 'M', age: 14, faltas: 20, nota_final: 4.0 }
      ]
      setStudents(mock)
      setFiltered(mock)
    }
  }

  useEffect(() => {
    const s = students.filter((st) => {
      const nameMatch = st.name.toLowerCase().includes(search.toLowerCase())
      const genderMatch = gender === 'all' ? true : st.gender === gender
      return nameMatch && genderMatch
    })
    setFiltered(s)
  }, [search, gender, students])

  async function handlePredict(student: any) {
    setSelectedStudent(student)
    setPredictLoading(true)
    setPrediction(null)
    try {
      const res = await fetch(`${API_BASE}/predict`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ student })
      })
      if (!res.ok) throw new Error('Erro na predição')
      const data = await res.json()
      setPrediction(data)
      setTab('predicao')
    } catch {
      const risk = Math.min(1, ((student.faltas || 0) / 30) * 0.6 + (Math.max(0, (8 - (student.nota_final || 6))) / 8) * 0.4)
      setPrediction({ risk, details: { fallback: true } })
      setTab('predicao')
    } finally {
      setPredictLoading(false)
    }
  }

  const riskBuckets = useMemo(() => {
    const counts = { low: 0, medium: 0, high: 0 }
    filtered.forEach((s) => {
      const r = Math.min(1, ((s.faltas || 0) / 30) * 0.6 + (Math.max(0, (8 - (s.nota_final || 6))) / 8) * 0.4)
      if (r < 0.33) counts.low++
      else if (r < 0.66) counts.medium++
      else counts.high++
    })
    return counts
  }, [filtered])

  const pieOption = {
    title: { text: 'Distribuição de Risco', left: 'center' },
    tooltip: { trigger: 'item' },
    series: [{
      name: 'Risco',
      type: 'pie',
      radius: '50%',
      data: [
        { value: riskBuckets.low, name: 'Baixo' },
        { value: riskBuckets.medium, name: 'Médio' },
        { value: riskBuckets.high, name: 'Alto' }
      ]
    }]
  }

  return (
    <div className="min-h-screen p-6">
      <div className="max-w-7xl mx-auto">
        <header className="flex items-center justify-between mb-6">
          <div>
            <h1 className="text-3xl font-bold">Sistema de Análise e Predição de Evasão Escolar</h1>
            <p className="text-gray-600">Painel de análise estatística e predição de evasão.</p>
          </div>
          <nav className="space-x-2">
            {['introducao', 'graficos', 'predicao'].map(t => (
              <button key={t} onClick={() => setTab(t)} className={`px-3 py-1 rounded ${tab === t ? 'bg-blue-600 text-white' : 'bg-white border'}`}>
                {t === 'introducao' ? 'Introdução' : t === 'graficos' ? 'Gráficos' : 'Predição'}
              </button>
            ))}
          </nav>
        </header>

        {tab === 'introducao' && (
          <section className="bg-white p-6 rounded shadow">
            <h2 className="text-2xl font-semibold mb-3">Introdução</h2>
            <p className="text-gray-700 mb-4">Explore os dados e identifique fatores que influenciam a evasão escolar.</p>
            <div className="flex gap-2">
              <button className="px-4 py-2 border rounded" onClick={() => setTab('graficos')}>Ver Gráficos</button>
              <button className="px-4 py-2 border rounded" onClick={() => setTab('predicao')}>Fazer Predição</button>
            </div>
          </section>
        )}

        {tab === 'graficos' && (
          <section className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
            <div className="lg:col-span-2 bg-white p-4 rounded shadow">
              <h3 className="font-semibold mb-3">Lista de Alunos ({filtered.length})</h3>
              <div className="flex gap-2 mb-3">
                <input value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Buscar por nome" className="border p-2 rounded flex-1" />
                <select value={gender} onChange={(e) => setGender(e.target.value)} className="border p-2 rounded">
                  <option value="all">Todos</option>
                  <option value="M">Masculino</option>
                  <option value="F">Feminino</option>
                </select>
              </div>

              <table className="w-full text-sm border-collapse">
                <thead>
                  <tr className="bg-gray-100">
                    <th className="border p-2">ID</th>
                    <th className="border p-2">Nome</th>
                    <th className="border p-2">Gênero</th>
                    <th className="border p-2">Idade</th>
                    <th className="border p-2">Faltas</th>
                    <th className="border p-2">Nota</th>
                    <th className="border p-2">Ações</th>
                  </tr>
                </thead>
                <tbody>
                  {filtered.map(s => (
                    <tr key={s.id} className="hover:bg-gray-50">
                      <td className="border p-2">{s.id}</td>
                      <td className="border p-2">{s.name}</td>
                      <td className="border p-2">{s.gender}</td>
                      <td className="border p-2">{s.age}</td>
                      <td className="border p-2">{s.faltas}</td>
                      <td className="border p-2">{s.nota_final}</td>
                      <td className="border p-2">
                        <button onClick={() => handlePredict(s)} className="px-3 py-1 border rounded">Ver risco</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <aside className="bg-white p-4 rounded shadow">
              <h3 className="font-semibold mb-3">Distribuição de Risco</h3>
              <div style={{ height: 280 }}>
                <ECharts option={pieOption} style={{ height: 260 }} />
              </div>
            </aside>
          </section>
        )}

        {tab === 'predicao' && prediction && (
          <section className="bg-white p-6 rounded shadow mb-6 text-center">
            <h2 className="text-xl font-semibold mb-3">Predição de Risco</h2>
            <div className="text-4xl font-bold text-blue-600">{Math.round((prediction.risk || 0) * 100)}%</div>
            <p className="text-gray-600 mt-2">Probabilidade estimada de evasão</p>
          </section>
        )}
      </div>
    </div>
  )
}
