export function InputPlateSearch() {
    return (
        <input
            type="text"
            name="plateSearch"
            id="plateSearch"
            placeholder="Digite a placa do veículo..."
            className="w-full sm:w-64 px-4 py-2 rounded-lg text-black placeholder-gray-500 
                 border border-gray-400 focus:border-[#FF6B00] focus:ring-2 focus:ring-[#FF6B00]/50 
                 transition-all duration-200 outline-none"
        />
    );
}
