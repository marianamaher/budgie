function saveEntry(newEntryValue){

    console.log(newEntryValue);

    $.ajax({
        type: "POST",
        url: "/saveEntry",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        complete: function(){
            $('.loadingDiv').hide();
        },
        data : JSON.stringify(newEntryValue),
        success: function(result){
            let all_data = result
            console.log(all_data)
            $.each(all_data, function(index, value){
                let tempDiv = ('<div class="resultDiv">' + value +'</div>')
                $(".budgetCalculatorContainer").append(tempDiv);
            });
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
        
    })

}

$(document).ready(function(){

    $("#firstName").focus();

        $("#budgetButton").click(function(ev){
            ev.preventDefault();
            // getting form information
            var username = $("#firstName").val();
            let userState = $("#state").val();
            let userIncome = $("#income").val();
            let fixedExpenses = $("#fixedExpenses").val();

            // saving information as a String object
            let budgetInformation = {name: username, state: userState, income: userIncome, expenses: fixedExpenses}

            //calling a function to save the information and send it to the server
            saveEntry( budgetInformation);
            // dealing with loading logo
            $(".budgetCalculatorContainer").empty();
            let tempDiv2 = ('<div class="loadingDiv"><img id="loadingLogo" src="/static/images/loading.gif"><br>Loading...</div>')
            $(".budgetCalculatorContainer").append(tempDiv2)
            
    
        })


});