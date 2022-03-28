console.log("js")
function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;

    return [year, month, day].join('-');
}

date = formatDate(new Date());
document.getElementById("id_payment_date").value = date;


$(document).on("change", ".amount_paid", function() {
    var sum = 0;
    $(".amount_paid").each(function(){
        sum += +$(this).val();
    });
    console.log(sum);
    $("#id_total_amount").val(sum);
});


function getProductDetails(stock){
        var product_id = document.getElementById("id_product_name").value;
        product_id = parseInt(product_id);
        {% for product in products %}
        if ({{ product.id}}==product_id)
        {
            var product_name = document.getElementById("hidden_product_name");
            var stock_value = document.getElementById("hidden_product_stock");
            product_name.value = "{{product.product_name}}";
            product_name.style.visibility = "visible";
            stock = "{{product.stock_available}}"+ " "+"{{product.unit}}"
            stock_value.value = stock;
            stock_value.style.visibility = "visible";
        }
        {% endfor %}
}
