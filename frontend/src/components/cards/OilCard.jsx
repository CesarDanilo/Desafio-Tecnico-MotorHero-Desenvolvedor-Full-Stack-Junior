import React from "react";

export function OilCard() {
    // Valores estáticos seguindo o modelo da imagem
    const oil = {
        name: "PREMIUM PROTECTION 5W-40",
        type: "Sintético – SN Plus",
        engineCapacity: 4.0,
        converter: 4000,
        bottleSize: 946,
        division: 4.23,
        total: 4730,
        leftover: 730,
        leftoverPercent: 18.25,
        image: "https://valvoline-oil.s3.amazonaws.com/products/ML9.jpg?AWSAccessKeyId=AKIA2KUKPWT5LNVRLPFF&Signature=%2BA%2Bs3AkAJxF4sRum11WrmmLhKHk%3D&Expires=1757604761"
    };

    return (
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4 max-w-md w-full shadow-md">
            {/* Imagem */}
            <div className="flex justify-center mb-4">
                <img
                    src={oil.image}
                    alt={oil.name}
                    className="h-16"
                />
            </div>

            {/* Nome e Tipo */}
            <h2 className="text-lg font-bold">{oil.name}</h2>
            <p className="text-gray-400 text-sm mb-4">{oil.type}</p>

            {/* Cálculo de frascos */}
            <div className="bg-gray-800 p-3 rounded mb-4">
                <p className="font-semibold mb-2">📊 CÁLCULO DE FRASCOS:</p>
                <p>Capacidade Motor: {oil.engineCapacity}L</p>
                <p>Converter: {oil.converter}ml</p>
                <p>Tamanho Frasco: {oil.bottleSize}ml</p>
                <p>Divisão: {oil.division.toFixed(2)}</p>
                <p>Total: {oil.total}ml</p>
                <p>Sobra: {oil.leftover}ml ({oil.leftoverPercent}%)</p>
            </div>

            {/* Botão */}
            <button className="w-full bg-orange-500 hover:bg-orange-600 text-white py-2 rounded font-semibold">
                Adicionar ao Orçamento
            </button>
        </div>
    );
}
