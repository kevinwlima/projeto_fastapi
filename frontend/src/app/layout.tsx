import './globals.css'

export const metadata = {
  title: 'Sistema de Análise e Predição de Evasão Escolar',
  description: 'Dashboard para análise e predição de evasão escolar'
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body className="bg-gray-50 text-gray-900">{children}</body>
    </html>
  )
}