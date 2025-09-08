export function VehicleCard({ vehicle }) {
    if (!vehicle) {
        return (
            <div className="bg-gray-900 border border-gray-800 rounded-lg p-4 max-w-md w-full shadow-md text-gray-400">
                Nenhum veículo consultado ainda.
            </div>
        )
    }

    const v = vehicle.data.data.vehicle
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

            {/* Detalhes técnicos */}
            <div className="text-gray-300 text-sm space-y-1 mb-3">
                <p>
                    <span className="font-medium text-white">Ano:</span>{" "}
                    {v.technical.year_manufacture}/{v.technical.year_model}
                </p>
                <p>
                    <span className="font-medium text-white">Motor:</span>{" "}
                    {v.technical.engine} {v.technical.fuel}
                </p>
                <p>
                    <span className="font-medium text-white">Capacidade:</span>{" "}
                    {v.technical.oil_capacity_liters} litros
                </p>
                <p>
                    <span className="font-medium text-white">Cidade:</span>{" "}
                    {v.location.city}/{v.location.state}
                </p>
            </div>

            {/* Restrições legais */}
            {v.legal.has_restrictions && v.legal.restrictions.length > 0 && (
                <div className="text-orange-500 font-semibold mb-3 flex items-center gap-1">
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
                </div>
            )}

        </div>
    )
}
