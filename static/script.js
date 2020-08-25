function send(){
    var number = document.getElementById("usr1").value
    var message = document.getElementById("usr2").value
    eel.send_sms(number,message)
    
}
eel.expose(sends); 
function sends(x){
    document.write(x);
    document.title="Status";
}
eel.expose(back);
function back(){
// Create anchor element. 
var a = document.createElement('a');              
// Create the text node for anchor element. 
var link = document.createTextNode("<<Back"); 
// Append the text node to anchor element. 
a.appendChild(link);  
// Set the href property. 
a.href = "index.html";  
// Append the anchor element to the body. 
document.body.appendChild(a);
}
