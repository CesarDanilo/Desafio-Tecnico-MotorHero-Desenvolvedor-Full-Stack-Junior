export function VehicleCard() {
    return (
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4 max-w-md w-full shadow-md">
            <div className="flex items-center gap-2 mb-2">
                <div className="p-2 bg-gray-800 rounded-full">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-6 w-6 text-gray-400"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M3 13l4-4 6 6 8-8"
                        />
                    </svg>
                </div>
                <h2 className="font-bold text-white text-lg">
                    RENAULT DUSTER ZEN 1.6
                    <span className="text-gray-400 ml-2">(ESS4H19 - ESS-4719)</span>
                </h2>
            </div>

            <div className="text-gray-300 text-sm space-y-1 mb-3">
                <p><span className="font-medium text-white">Ano:</span> 2020/2021</p>
                <p><span className="font-medium text-white">Motor:</span> 1.6 FLEX</p>
                <p><span className="font-medium text-white">Capacidade:</span> 4.0 litros</p>
                <p><span className="font-medium text-white">Cidade:</span> Ribeirão Preto/SP</p>
            </div>

            <div className="text-orange-500 font-semibold mb-3 flex items-center gap-1">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-5 w-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                >
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01M12 2a10 10 0 1010 10A10 10 0 0012 2z" />
                </svg>
                ALIENAÇÃO FIDUCIÁRIA
            </div>

            <div className="text-gray-300 text-sm space-y-1">
                <p className="font-semibold text-white">VALORES:</p>
                <p>• Unitário: R$ 52,90 | Total (5x): R$ 264,50</p>
                <p>• Seu lucro: R$ 65,00 | Margem: 32.6%</p>
            </div>
        </div>
    );
}
