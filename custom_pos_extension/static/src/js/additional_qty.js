/** @odoo-module **/

function updateAdditionalPrice() {

    const qtyInput = document.querySelector(".js_add_qty_input");
    const priceDisplay = document.querySelector(".js_additional_price_display");
    const unitPriceInput = document.querySelector(".js_product_unit_price");
    const hiddenQtyInput = document.querySelector(".js_additional_qty_hidden");

    if (qtyInput && priceDisplay && unitPriceInput) {
        const unitPrice = parseFloat(unitPriceInput.value) || 0;
        const qty = parseInt(qtyInput.value) || 0;


        const totalExtra = unitPrice * qty;
        priceDisplay.innerText = totalExtra.toFixed(2);

        if (hiddenQtyInput) {
            hiddenQtyInput.value = qty;
        }
    }
}

document.addEventListener("click", function (ev) {
    const qtyInput = document.querySelector(".js_add_qty_input");
    if (!qtyInput) return;

    if (ev.target.closest(".js_add_qty_plus")) {
        qtyInput.value = parseInt(qtyInput.value || 0) + 1;
        updateAdditionalPrice();
    }

    if (ev.target.closest(".js_add_qty_minus")) {
        qtyInput.value = Math.max(0, parseInt(qtyInput.value || 0) - 1);
        updateAdditionalPrice();
    }
});