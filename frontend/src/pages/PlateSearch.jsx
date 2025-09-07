import { InputPlateSearch } from "../components/Input/Input-PlateSearch"
import { ButtonSubmit } from "../components/buttons/button-submit"
import { CheckCircle2, XCircle } from "lucide-react"
import { VehicleCard } from "../components/cards/VehicleCard"
import { OilCard } from "../components/cards/OilCard"
import axios from "axios"
import { useState } from "react"

export default function PlateSearch() {
    const [plate, setPlate] = useState("")
    const [isValid, setIsValid] = useState(null)

    async function handleSubmit(e) {
        const data = await fetchVehicleData(plate)
        console.log(data)
    }

    async function fetchVehicleData(plate) {
        const data = {
            plate: plate,
            mechanic_id: "mech_001"
        }
        try {
            const response = await axios.post(`http://127.0.0.1:8000/api/vehicle/consult`, data)
            return response.data
        } catch (error) {
            console.error("Error fetching vehicle data:", error)
            throw error
        }
    }

    function ValidationMessage({ isValid, message }) {
        if (isValid === null) return null // não mostra nada se ainda não validado

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

            <div className="flex gap-2 w-full sm:w-auto">
                <InputPlateSearch setPlate={setPlate} />
                <ButtonSubmit label={"Consultar"} handleSubmit={handleSubmit} />
            </div>

            <div className="w-full max-w-sm flex justify-start mt-2">
                <ValidationMessage isValid={true} />
            </div>

            <div className="mt-6 w-full max-w-4xl grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="bg-gray-900 rounded-lg p-4 border border-gray-800">
                    <VehicleCard />
                </div>
                <div className="bg-gray-900 rounded-lg p-4 border border-gray-800">
                    <OilCard />
                </div>
            </div>
        </div>
    )
}
