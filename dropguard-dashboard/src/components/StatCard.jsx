export default function StatCard({ title, value, color }) {
  return (
    <div className={`bg-white p-6 rounded-xl shadow-md border-l-4 ${color}`}>
      <h3 className="text-gray-500 text-sm">{title}</h3>
      <p className="text-3xl font-bold mt-2">{value}</p>
    </div>
  )
}