
function Nome(props){
    
    return(
        
        <div>
            <h3> Meu nome é {props.nome}</h3>
        </div>
    );
}




//HOOKS
function Hooks() {

    const[nome,setNome]= React.useState(["Santo","Eder"]);

    let newname = "";

    function  addnome(e) {
        
        newname=e.target.value;
        

    }
   
    return(
        <div>
            <input id="entrada" type="text" onChange={addnome} />
            <button onClick={()=>{
               if(newname===""){
                   alert("Digite um nome válido!")
               } 
               else{
                    let novonome= [...nome,newname];
                    setNome(novonome);
                    newname="";
                    document.getElementById("entrada").value="";   
               }          
                             
            }}>
                Add nome
            </button>
            <ul>
                {nome.map(item =>{
                   return <li key={item}>{item}</li>
                })}
            </ul>
            
        </div>

    );
    
}


const MeuContainer = document.getElementById('root');

ReactDOM.render(<Hooks />, MeuContainer);
