import { motion } from "framer-motion";
import { useEffect, useState } from "react";

// Função para obter contagem do localStorage
function getQueryCounts() {
    const now = new Date();
    const todayKey = `queryCount_${now.toISOString().slice(0, 10)}`;
    const weekKey = `queryCount_week_${getWeekNumber(now)}`;

    const today = parseInt(localStorage.getItem(todayKey)) || 0;
    const week = parseInt(localStorage.getItem(weekKey)) || 0;

    return { today, week };
}

function getWeekNumber(date) {
    const tempDate = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
    const dayNum = tempDate.getUTCDay() || 7;
    tempDate.setUTCDate(tempDate.getUTCDate() + 4 - dayNum);
    const yearStart = new Date(Date.UTC(tempDate.getUTCFullYear(), 0, 1));
    return Math.ceil((((tempDate - yearStart) / 86400000) + 1) / 7);
}

export function CardsConsultas() {
    const [counts, setCounts] = useState({ today: 0, week: 0 });

    useEffect(() => {
        setCounts(getQueryCounts());
        const interval = setInterval(() => {
            setCounts(getQueryCounts());
        }, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="flex flex-wrap gap-4 mb-8 justify-center sm:justify-start">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8 }}
            >
                <div className="border border-gray-400 rounded-md p-4 w-32 text-center">
                    <p className="text-sm text-gray-500">Hoje</p>
                    <p className="text-2xl font-bold">{counts.today}</p>
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
                    <p className="text-2xl font-bold">{counts.week}</p>
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
