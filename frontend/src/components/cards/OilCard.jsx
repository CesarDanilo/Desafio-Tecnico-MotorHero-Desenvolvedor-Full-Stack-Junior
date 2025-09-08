import React from "react";

export function OilCard({ oilData }) {
    const oilFromProps = oilData?.data?.data?.oil_recommendation;
    const calc = oilFromProps?.calculation;

    const unit_price = 52.90;
    const unit_cost = 36.00;

    const bottles_needed = calc?.bottles_needed ?? 0;

    const total_price = bottles_needed * unit_price;
    const total_cost = bottles_needed * unit_cost;
    const profit = total_price - total_cost;
    const margin = total_price > 0 ? (profit / total_price) * 100 : 0;

    if (!oilFromProps) {
        return (
            <div className="bg-gray-900 border border-gray-800 rounded-lg p-4 max-w-md w-full shadow-md text-gray-400">
                Nenhuma recomendação de óleo disponível.
            </div>
        );
    }

    return (
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4 max-w-md w-full shadow-md text-white">
            {/* Cabeçalho */}
            <div className="flex justify-start items-center mb-4">
                <img
                    src={oilFromProps.product.image_url}
                    alt={oilFromProps.product.name}
                    className="h-16 w-16 object-contain"
                />
                <div className="flex flex-col justify-center ml-4">
                    <h2 className="text-lg font-bold">{oilFromProps.product.name}</h2>
                    <p className="text-gray-400 text-sm">{oilFromProps.product.type}</p>
                </div>
            </div>

            {calc && (
                <div className="bg-gray-800 p-3 rounded mb-4 text-gray-300 text-sm">
                    <p className="font-semibold mb-2">📊 CÁLCULO DE FRASCOS:</p>
                    <p>Capacidade Motor: {(calc.engine_capacity_ml / 1000).toFixed(1)} L</p>
                    <p>Tamanho do Frasco: {calc.bottle_size_ml} ml</p>
                    <p>Frascos Necessários: {calc.bottles_needed}</p>
                    <p>Fórmula: {calc.math_formula}</p>
                    <p>Total: {calc.total_volume_ml} ml</p>
                    <p>Sobra: {calc.excess_ml} ml ({calc.excess_percentage}%)</p>
                </div>
            )}

            <div className="bg-gray-800 p-3 rounded mb-4 text-gray-300 text-sm">
                <ul>
                    <li>💰 <strong>VALORES:</strong></li>
                    <li>• Unitário: R$ {unit_price.toFixed(2).replace('.', ',')}</li>
                    <li>• Total ({bottles_needed}x): R$ {total_price.toFixed(2).replace('.', ',')}</li>
                    <li>• Seu lucro: R$ {profit.toFixed(2).replace('.', ',')}</li>
                    <li>• Margem: {margin.toFixed(1).replace('.', ',')}%</li>
                </ul>
            </div>

            <button className="w-full bg-orange-500 hover:bg-orange-600 text-white py-2 rounded font-semibold">
                Adicionar ao Orçamento
            </button>
        </div>
    );
}
