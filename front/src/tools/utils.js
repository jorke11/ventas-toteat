export const formatNumber = (number) => {
    number = parseFloat(number).toFixed(3)
    return new Intl.NumberFormat('es-ES').format(number)
}