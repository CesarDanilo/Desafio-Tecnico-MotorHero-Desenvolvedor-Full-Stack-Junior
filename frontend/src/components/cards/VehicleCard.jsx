import { motion } from "framer-motion"

export function VehicleCard({ vehicle }) {
    if (!vehicle) {
        return (
            <div className="bg-gray-900 border border-gray-800 rounded-lg p-4 max-w-md w-full shadow-md text-gray-400">
                Nenhum veículo consultado ainda.
            </div>
        )
    }

    const v = vehicle.data.data.vehicle

    // passos que serão animados
    const details = [
        `Ano: ${v.technical.year_manufacture}/${v.technical.year_model}`,
        `Motor: ${v.technical.engine} ${v.technical.fuel}`,
        `Capacidade: ${v.technical.oil_capacity_liters} litros`,
        `Cidade: ${v.location.city}/${v.location.state}`
    ]

    return (
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4 max-w-md w-full shadow-md">
            {/* Título com logo */}
            <div className="flex items-center gap-2 mb-2">
                <div className="p-2 bg-gray-800 rounded-full">
                    <img
                        src={v.identification.logo}
                        alt={v.identification.brand}
                        className="h-6 w-6 object-contain"
                    />
                </div>
                <h2 className="font-bold text-white text-lg">
                    {v.identification.brand} {v.identification.pretty_name}
                    <span className="text-gray-400 ml-2">
                        ({v.identification.plate})
                    </span>
                </h2>
            </div>

            {/* Detalhes técnicos animados */}
            <div className="text-gray-300 text-sm space-y-1 mb-3">
                {details.map((detail, index) => (
                    <motion.p
                        key={index}
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: index * 0.3, duration: 0.5 }}
                    >
                        {detail}
                    </motion.p>
                ))}
            </div>

            {/* Restrições legais animadas */}
            {v.legal.has_restrictions && v.legal.restrictions.length > 0 && (
                <motion.div
                    initial={{ opacity: 0, y: -10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: details.length * 0.3 }}
                    className="text-orange-500 font-semibold mb-3 flex items-center gap-1"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-5 w-5"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M12 9v2m0 4h.01M12 2a10 10 0 1010 10A10 10 0 0012 2z"
                        />
                    </svg>
                    {v.legal.restrictions.join(", ")}
                </motion.div>
            )}
        </div>
    )
}
