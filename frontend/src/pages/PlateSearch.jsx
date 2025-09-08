import { InputPlateSearch } from "../components/Input/Input-PlateSearch"
import { ButtonSubmit } from "../components/buttons/button-submit"
import { VehicleCard } from "../components/cards/VehicleCard"
import { OilCard } from "../components/cards/OilCard"
import { useState } from "react"
import { fetchVehicle } from "../functions/fetchVehicleData"
import { ValidationMessage } from "../components/validation-message/Validation-message"
import { motion } from "framer-motion"
import { ModalQuote } from "../components/modal/dialog-quote"

export default function PlateSearch() {
    const [plate, setPlate] = useState("")
    const [isValid, setIsValid] = useState(null)
    const [vehicleData, setVehicleData] = useState(null)
    const [oilData, setOilData] = useState(null)
    const [open, setOpen] = useState(false)

    async function handleSubmit(e) {
        e.preventDefault()
        try {
            const data = await fetchVehicle(plate)
            console.log("Dados recebidos:", data)
            setVehicleData(data)
            setOilData(data)
            setIsValid(true)
        } catch (error) {
            setIsValid(false)
        }
    }

    function handleOpenDialog(open) {
        setOpen(true)
    }

    function handleCloseDialog(close) {
        setOpen(false)
    }

    return (
        <div className="flex flex-col items-center justify-center min-h-screen p-5 bg-gray-950 text-white">
            {open && <ModalQuote isOpen={open} handleCloseDialog={handleCloseDialog} />}
            <form onSubmit={handleSubmit} className="flex gap-2 w-full sm:w-auto">
                <InputPlateSearch setPlate={setPlate} />
                <ButtonSubmit label="Consultar" />
            </form>

            <div className="w-full max-w-sm flex justify-start mt-2">
                <ValidationMessage isValid={isValid} />
            </div>

            <div className="mt-6 w-full max-w-4xl grid grid-cols-1 sm:grid-cols-2 gap-4">
                {vehicleData ? (
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.6 }}
                        className="bg-gray-900 rounded-lg p-4 border border-gray-800"
                    >
                        <VehicleCard vehicle={vehicleData} />
                    </motion.div>
                ) : (
                    <p className="text-gray-400">Nenhum veículo consultado ainda.</p>
                )}

                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.3 }}
                    className="bg-gray-900 rounded-lg p-4 border border-gray-800"
                >
                    <OilCard oilData={oilData} handleOpenDialog={handleOpenDialog} />
                </motion.div>
            </div>
        </div>
    )
}
