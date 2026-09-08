import axios from 'https://cdn.jsdelivr.net/npm/axios@1.20.0/+esm';

const dailyAverage = document.getElementById("daily-average")
const topSpikes = document.getElementById("top-spikes")
const anomalies = document.getElementById("anomalies")
const loading = document.querySelectorAll(".loading")

class HttpException extends Error{
    constructor(statusCode, message){
        super(message);
        this.name="HttpError";
        this.statusCode=statusCode;
    }
}

axios.get("data/energy_stats.json")
    .then((response)=>{
        const data=response.data;

        dailyAverage.textContent=data['daily_average'];

        topSpikes.innerHTML="";

        data.top_spikes.forEach((spike) => {
            const card = document.createElement("div");

            card.classList.add("card");

            card.innerHTML=`
            <h3>${spike.timestamp}</h3>
            <p>Price: ${spike.price}</p>
            `;
            
            topSpikes.appendChild(card);
        });
        
        anomalies.innerHTML=""
        data.anomalies.forEach((anomaly)=>{
            const card=document.createElement("div");
            
            card.classList.add("card");

            card.innerHTML=`
            <h3>${anomaly.timestamp}</h3>
            <p>Price: ${anomaly.price}</p>
            `;

            anomalies.appendChild(card);
        })

    })
    .catch(error=>{

        if(error.message){
            loading.forEach((element)=>{
                element.textContent=`${error.message}`
            })
        }
        
        console.error(error.message);
    })

   


