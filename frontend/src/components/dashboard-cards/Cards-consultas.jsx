import { motion } from "framer-motion";

export function CardsConsultas() {
    return (
        <div className="flex flex-wrap gap-4 mb-8 justify-center sm:justify-start">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8 }}
            >
                <div className="border border-gray-400 rounded-md p-4 w-32 text-center">
                    <p className="text-sm text-gray-500">Hoje</p>
                    <p className="text-2xl font-bold">15</p>
                    <p className="text-sm text-gray-500">consultas</p>
                </div>
            </motion.div>

            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 1 }}
            >
                <div className="border border-gray-400 rounded-md p-4 w-32 text-center">
                    <p className="text-sm text-gray-500">Semana</p>
                    <p className="text-2xl font-bold">89</p>
                    <p className="text-sm text-gray-500">consultas</p>
                </div>
            </motion.div>

            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 1.1 }}
            >
                <div className="border border-gray-400 rounded-md p-4 w-32 text-center">
                    <p className="text-sm text-gray-500">Top Marca</p>
                    <p className="text-2xl font-bold">VW</p>
                    <p className="text-sm text-gray-500">34%</p>
                </div>
            </motion.div>

            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 1.2 }}
            >
                <div className="border border-gray-400 rounded-md p-4 w-32 text-center">
                    <p className="text-sm text-gray-500">Óleo + Usado</p>
                    <p className="text-2xl font-bold">5W-40</p>
                    <p className="text-sm text-gray-500">67%</p>
                </div>
            </motion.div>
        </div>
    );
}
