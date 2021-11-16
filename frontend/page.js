//jquery page

//global variables
let runningWindow;



//main
$(document).ready(function (){

    runningMan();

});

//add functions here to modify gif

//move the player
function runningMan(){

    runningWindow = $('.runningGif');
    let marginLeft = 0;
    let maxMargin = 800;
    let currentMargin = marginLeft;

    setInterval(function(){

        //update the css property every 1 ms
        if(currentMargin > maxMargin){
            currentMargin = 0;
        }

        runningWindow.css('margin-left', currentMargin);

        currentMargin = currentMargin + 1;



    },10);
    //repeat every 1 ms
}//function to move man
