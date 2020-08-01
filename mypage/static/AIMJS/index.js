var tab_elements = document.querySelectorAll(".tab-bar ul li");
var item_elements = document.querySelectorAll(".containers");
for(var i = 0; i < tab_elements.length; i++){
    tab_elements[i].addEventListener("click", function(){
        tab_elements.forEach(function(li){
            li.classList.remove("active");
        })
        this.classList.add("active");
        var tab_value = this.getAttribute("data-li");
        // console.log(item_elements[0].style.display="none")
        item_elements.forEach(function(containers){
            containers.style.display = "none";
        })
        if(tab_value == "tab1"){
            document.querySelector("." + tab_value).style.display="flex";
        }
        if(tab_value == "tab2"){
            document.querySelector("." + tab_value).style.display="flex";
                    }
        if(tab_value == "tab3"){
            document.querySelector("." + tab_value).style.display="flex";
        }
        else{
            console.log("error");
        }
    })
}