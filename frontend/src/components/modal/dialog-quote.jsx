import { useState } from "react"

export function ModalQuote({ isOpen, handleCloseDialog, vehicleData }) {
    if (!isOpen) return null

    const plate = vehicleData.data.data.vehicle.identification.plate
    const oilname = vehicleData.data.data.oil_recommendation.product.name
    const amount = vehicleData.data.data.oil_recommendation.calculation.bottles_needed

    const [checked, setChecked] = useState(true)
    const [discount, setDiscount] = useState(5)

    const unitPrice = 52.9
    const subtotal = checked ? amount * unitPrice : 0

    const total = subtotal - (subtotal * discount) / 100

    return (
        <div className="fixed inset-0 flex items-center justify-center bg-black/50 backdrop-blur-sm z-50">
            <div className="bg-white/10 backdrop-blur-lg border border-white/20 shadow-xl rounded-2xl p-6 w-full max-w-md text-gray-200">

                <h2 className="text-lg font-bold mb-4 text-center">
                    Criar Orçamento – {plate}
                </h2>

                <div className="space-y-3 mb-4">
                    <input
                        type="text"
                        placeholder="Cliente"
                        className="w-full px-3 py-2 rounded-lg bg-white/10 border border-white/20 focus:outline-none focus:ring-2 focus:ring-blue-400"
                    />
                    <input
                        type="tel"
                        placeholder="Telefone"
                        className="w-full px-3 py-2 rounded-lg bg-white/10 border border-white/20 focus:outline-none focus:ring-2 focus:ring-blue-400"
                    />
                </div>

                <div className="mb-4">
                    <h3 className="font-semibold mb-2">Itens:</h3>
                    <div className="flex justify-between">
                        <label className="flex items-center gap-2">
                            <input
                                type="checkbox"
                                checked={checked}
                                onChange={(e) => setChecked(e.target.checked)}
                            />
                            {oilname} ({amount}un)
                        </label>
                        <span>
                            R$ {(amount * unitPrice).toFixed(2).replace(".", ",")}
                        </span>
                    </div>
                </div>

                <div className="flex items-center justify-between mb-4">
                    <label className="font-semibold">Desconto:</label>
                    <input
                        type="number"
                        value={discount}
                        onChange={(e) => setDiscount(Number(e.target.value))}
                        className="w-16 px-2 py-1 rounded bg-white/10 border border-white/20 text-center"
                    />
                    <span>%</span>
                </div>

                {checked && (
                    <div className="text-right font-bold text-lg mb-6">
                        TOTAL: R$ {total.toFixed(2).replace(".", ",")}
                    </div>
                )}

                <div className="flex justify-between">
                    <button
                        onClick={handleCloseDialog}
                        className="px-4 py-2 rounded-lg bg-red-500/80 hover:bg-red-500 transition"
                    >
                        Cancelar
                    </button>
                    <button className="px-4 py-2 rounded-lg bg-green-500/80 hover:bg-green-500 transition">
                        Gerar Orçamento
                    </button>
                </div>
            </div>
        </div>
    )
}
