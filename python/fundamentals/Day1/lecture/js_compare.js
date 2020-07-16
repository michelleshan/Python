function return_a_variable(){
    var strAndNum = 'Day' + 1;
    var myVariable = 10;
    return myVariable;
}
        console.log(return_a_variable());

function ifStatement(){

}

function forLoops(arr){
    arr.pop();
    arr.push(6);
    for(var i=0;i<arr.length;i++){
        console.log(arr[i]);
    }
    for(var i=0;i<arr.length;i++){
        console.log(arr[i]);
    }
}
forLoops([3,7,2,9]);