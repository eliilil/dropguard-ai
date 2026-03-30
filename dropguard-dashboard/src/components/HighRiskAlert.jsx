export default function HighRiskAlert({ students }) {

  if (!students || students.length === 0) return null

  return (
    <div className="bg-red-100 border border-red-300 p-4 rounded-lg mb-6">

      <h2 className="text-red-700 font-bold">
        ⚠ High Risk Students ({students.length})
      </h2>

      <div className="mt-2 space-y-1 max-h-40 overflow-y-auto">

        {students.slice(0,10).map((s)=>(
          <div key={s.student_id} className="text-sm">
            {s.name} • Burnout: {s.burnout_risk} • Sleep: {s.avg_sleep_hours}
          </div>
        ))}

      </div>

    </div>
  )
}