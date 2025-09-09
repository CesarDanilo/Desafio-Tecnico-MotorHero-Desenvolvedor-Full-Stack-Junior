import axios from "axios";

export async function fetchVehicle(plate) {
    const url = import.meta.env.VITE_API_URL
    console.log("URL:", url)
    const payload = {
        plate,
        mechanic_id: "mech_001"
    };

    try {
        const response = await axios.post(
            `${url}/api/vehicle/consult`,
            payload
        );
        return { data: response.data, error: null };
    } catch (error) {
        let message = "Ocorreu um erro ao consultar o veículo.";

        if (error.response) {
            // Erro retornado pela API
            console.error("Erro na resposta da API:", error.response.data);

            if (error.response.data && error.response.data.detail) {
                message = error.response.data.detail;
            }
        } else if (error.request) {
            console.error("Nenhuma resposta recebida:", error.request);
            message = "Não foi possível conectar ao servidor.";
        } else {
            console.error("Erro ao configurar requisição:", error.message);
            message = error.message;
        }

        return { data: null, error: message };
    }
}
