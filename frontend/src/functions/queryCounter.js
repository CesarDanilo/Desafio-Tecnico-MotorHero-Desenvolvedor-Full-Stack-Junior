export function queryCounter() {
    const now = new Date();
    const todayKey = `queryCount_${now.toISOString().slice(0, 10)}`; // Ex: 'queryCount_2025-09-08'
    const weekKey = `queryCount_week_${getWeekNumber(now)}`; // Ex: 'queryCount_week_36'

    // Recupera valores atuais do localStorage
    const todayCount = parseInt(localStorage.getItem(todayKey)) || 0;
    const weekCount = parseInt(localStorage.getItem(weekKey)) || 0;

    // Incrementa
    localStorage.setItem(todayKey, todayCount + 1);
    localStorage.setItem(weekKey, weekCount + 1);

    // Retorna os contadores atualizados
    return {
        today: todayCount + 1,
        week: weekCount + 1
    };
}

// Função auxiliar para obter o número da semana do ano
function getWeekNumber(date) {
    const tempDate = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
    const dayNum = tempDate.getUTCDay() || 7;
    tempDate.setUTCDate(tempDate.getUTCDate() + 4 - dayNum);
    const yearStart = new Date(Date.UTC(tempDate.getUTCFullYear(), 0, 1));
    return Math.ceil((((tempDate - yearStart) / 86400000) + 1) / 7);
}
