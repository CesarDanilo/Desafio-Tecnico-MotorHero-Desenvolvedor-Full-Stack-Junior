import axios from "axios"

export async function createQuotes({ data }) {
    const url = import.meta.env.VITE_API_URL

    const quoteData = {
        vehicle_description: data.vehicle_description,
        plate: data.plate,
        customer_name: data.customer_name,
        customer_phone: data.customer_phone,
        mechanic_id: "1",
        items: [
            {
                type: data.items[0].type,
                code: data.items[0].code,
                description: data.items[0].description,
                quantity: data.items[0].quantity,
                unit_price: data.items[0].unit_price,
            },
        ],
        discount_percentage: data.discount_percentage,
    }

    try {
        const response = await axios.post(url+"/api/quote/create", quoteData, {
            headers: {
                "Content-Type": "application/json",
            },
        });

        return response.data
    } catch (error) {
        console.error("Erro ao criar orçamento:", error.response?.data || error.message)
        throw error
    }
}
