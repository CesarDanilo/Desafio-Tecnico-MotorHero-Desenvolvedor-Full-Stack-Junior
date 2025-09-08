import { CheckCircle2, XCircle } from "lucide-react"

export function ValidationMessage({ isValid, message }) {
    if (isValid === null) return null

    return (
        <div
            className={`flex items-center gap-2 mt-2 text-sm font-medium transition-all duration-200
        ${isValid ? "text-green-500" : "text-red-500"}`}
        >
            {isValid ? (
                <CheckCircle2 className="w-5 h-5" />
            ) : (
                <XCircle className="w-5 h-5" />
            )}
            <span>{message || (isValid ? "Formato válido" : "Formato inválido")}</span>
        </div>
    )
}