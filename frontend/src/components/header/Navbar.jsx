import { useState } from "react";
import { Loader2 } from "lucide-react";

export function Navbar() {
    const [consultas, setConsultas] = useState(15);
    const [loading, setLoading] = useState(false);

    return (
        <nav className="w-full bg-gray-900 text-white shadow-md sticky top-0 z-50">
            <div className="max-w-7xl mx-auto flex items-center justify-between px-4 py-3 sm:px-6 lg:px-8">

                {/* Logo */}
                <div className="flex items-center space-x-2">
                    <div className="text-xl font-bold text-[#FF6B00]">MotorHero</div>
                </div>

                {/* Título */}
                <div className="hidden md:block">
                    <p className="text-sm sm:text-base text-gray-300">
                        Sistema de Consulta e Orçamento
                    </p>
                </div>

                {/* Contador */}
                <div className="flex items-center space-x-2">
                    {loading ? (
                        <Loader2 className="w-5 h-5 animate-spin text-[#FF6B00]" />
                    ) : (
                        <span className="text-sm sm:text-base font-semibold">
                            <span className="text-gray-300">Consultas hoje: </span>
                            <span className="text-[#FF6B00]">{consultas}</span>
                        </span>
                    )}
                </div>
            </div>
        </nav>
    );
}
