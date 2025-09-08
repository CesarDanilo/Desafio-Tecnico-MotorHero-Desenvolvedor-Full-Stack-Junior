import { InputPlateSearch } from "../components/Input/Input-PlateSearch"
import { ButtonSubmit } from "../components/buttons/button-submit"
import { CheckCircle2, XCircle } from "lucide-react"
import { VehicleCard } from "../components/cards/VehicleCard"
import { OilCard } from "../components/cards/OilCard"
import { useState } from "react"
import { fetchVehicle } from "../functions/fetchVehicleData"

export default function PlateSearch() {
    const [plate, setPlate] = useState("")
    const [isValid, setIsValid] = useState(null)
    const [vehicleData, setVehicleData] = useState(null) // guarda dados do veículo

    async function handleSubmit(e) {
        e.preventDefault()
        try {
            const data = await fetchVehicle(plate)
            console.log("Dados recebidos:", data)
            setVehicleData(data) // salva dados para enviar ao card
            setIsValid(true)
        } catch (error) {
            setIsValid(false)
        }
    }

    function ValidationMessage({ isValid, message }) {
        if (isValid === null) return null

        return (
            <div
                className={`flex items-center gap-2 mt-2 text-sm font-medium transition-all duration-200
        ${isValid ? "text-green-500" : "text-red-500"}`}
            >
                {isValid ? (
                    <CheckCircle2 className="w-5 h-5" />
                ) : (
                    <XCircle className="w-5 h-5" />
                )}
                <span>{message || (isValid ? "Formato válido" : "Formato inválido")}</span>
            </div>
        )
    }

    return (
        <div className="flex flex-col items-center justify-center min-h-screen p-5 bg-gray-950 text-white">

            <form onSubmit={handleSubmit} className="flex gap-2 w-full sm:w-auto">
                <InputPlateSearch setPlate={setPlate} />
                <ButtonSubmit label="Consultar" />
            </form>

            <div className="w-full max-w-sm flex justify-start mt-2">
                <ValidationMessage isValid={isValid} />
            </div>

            <div className="mt-6 w-full max-w-4xl grid grid-cols-1 sm:grid-cols-2 gap-4">
                {vehicleData ? (
                    <div className="bg-gray-900 rounded-lg p-4 border border-gray-800">
                        <VehicleCard vehicle={vehicleData} />
                    </div>
                ) : (
                    <p className="text-gray-400">Nenhum veículo consultado ainda.</p>
                )}
                <div className="bg-gray-900 rounded-lg p-4 border border-gray-800">
                    <OilCard />
                </div>
            </div>
        </div>
    )
}
