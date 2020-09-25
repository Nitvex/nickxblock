/* Javascript for NikitaXBlock. */
function NikitaXBlock(runtime, element) {

    function showAlert(result) {
        const span = document.querySelector("count");
        span.innerText = `you scored ${result.result} out of 10`;
        alert(JSON.stringify(result));
    }

    var handlerUrl = runtime.handlerUrl(element, 'check');

    $('button', element).click(function(event) {
        const input = document.querySelector("input");
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({ data: input.value}),
            success: showAlert
        });
    })

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
