export function ButtonSubmit({ label }) {
    return (
        <button
            type="submit"
            className="w-full sm:w-auto px-6 py-2 rounded-lg 
                 bg-[#FF6B00] text-white font-medium 
                 hover:bg-[#e65f00] active:scale-95 
                 transition-all duration-200 
                 focus:outline-none focus:ring-2 focus:ring-[#FF6B00]/50"
        >
            {label}
        </button>
    );
}
