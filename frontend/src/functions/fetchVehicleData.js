import axios from "axios"

export async function fetchVehicle(plate) {
    const payload = {
        plate,
        mechanic_id: "mech_001"
    }

    try {
        const response = await axios.post("http://127.0.0.1:8000/api/vehicle/consult", payload)
        return response.data
    } catch (error) {
        if (error.response) {
            console.error("Erro na resposta da API:", error.response.data)
        } else if (error.request) {
            console.error("Nenhuma resposta recebida:", error.request)
        } else {
            console.error("Erro ao configurar requisição:", error.message)
        }
        throw error
    }
}