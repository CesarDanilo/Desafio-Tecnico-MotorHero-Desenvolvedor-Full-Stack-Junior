import { InputPlateSearch } from "../components/Input/Input-PlateSearch";
import { ButtonSubmit } from "../components/buttons/button-submit";
import { VehicleCard } from "../components/cards/VehicleCard";
import { OilCard } from "../components/cards/OilCard";
import { useState } from "react";
import { fetchVehicle } from "../functions/fetchVehicleData";
import { ValidationMessage } from "../components/validation-message/Validation-message";
import { motion } from "framer-motion";
import { ModalQuote } from "../components/modal/dialog-quote";
import { CardsConsultas } from "../components/dashboard-cards/CardsConsultas";
import { queryCounter } from "../functions/queryCounter";

export default function PlateSearch() {
    const [plate, setPlate] = useState("");
    const [isValid, setIsValid] = useState(null);
    const [vehicleData, setVehicleData] = useState(null);
    const [oilData, setOilData] = useState(null);
    const [open, setOpen] = useState(false);
    const [toast, setToast] = useState(null); 

    function showToast(message) {
        setToast({ message });
        setTimeout(() => {
            setToast(null);
        }, 4000); 
    }

    async function handleSubmit(e) {
        e.preventDefault();
        try {
            const { data, error } = await fetchVehicle(plate);

            if (data == null) {
                setIsValid(false);
                if (error) showToast(error);
                return;
            }

            if (error) {
                showToast(error);
                return;
            }

            queryCounter()
            setVehicleData(data);
            setOilData(data);
            setIsValid(true);
        } catch (error) {
            setIsValid(false);
            showToast("Ocorreu um erro inesperado.");
        }
    }

    function handleOpenDialog() {
        setOpen(true);
    }

    function handleCloseDialog() {
        setOpen(false);
    }

    return (
        <div className="flex flex-col items-center justify-center min-h-screen p-5 bg-gray-950 text-white relative">
            {open && (
                <ModalQuote
                    isOpen={open}
                    handleCloseDialog={handleCloseDialog}
                    vehicleData={vehicleData}
                    oilData={oilData}
                />
            )}
            <CardsConsultas />
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

            {toast && (
                <div className="fixed bottom-5 right-5 bg-red-600 text-white px-4 py-2 rounded shadow-lg animate-slideIn">
                    {toast.message}
                </div>
            )}
        </div>
    );
}
