import React from "react";

export function OilCard({ oilData }) {
    const oilFromProps = oilData?.data?.data?.oil_recommendation;

    if (!oilFromProps) {
        return (
            <div className="bg-gray-900 border border-gray-800 rounded-lg p-4 max-w-md w-full shadow-md text-gray-400">
                Nenhuma recomendação de óleo disponível.
            </div>
        );
    }

    const calc = oilFromProps.calculation;

    return (
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4 max-w-md w-full shadow-md">

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

            {/* Cálculo de frascos */}
            <div className="bg-gray-800 p-3 rounded mb-4 text-gray-300 text-sm">
                <p className="font-semibold mb-2">📊 CÁLCULO DE FRASCOS:</p>
                <p>Capacidade Motor: {calc.engine_capacity_ml / 1000} L</p>
                <p>Tamanho do Frasco: {calc.bottle_size_ml} ml</p>
                <p>Barris Necessários: {calc.bottles_needed}</p>
                <p>Fórmula: {calc.math_formula}</p>
                <p>Total: {calc.total_volume_ml} ml</p>
                <p>Sobra: {calc.excess_ml} ml ({calc.excess_percentage}%)</p>
            </div>

            <button className="w-full bg-orange-500 hover:bg-orange-600 text-white py-2 rounded font-semibold">
                Adicionar ao Orçamento
            </button>
        </div>
    );
}
