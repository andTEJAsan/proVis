// import st from "../../../styles/dashboard/card.module.css"


// obj = {company_img_url : data.company_img_url , 
//     //   product_img_url : data.product_img_url,
//     //   description : data.description , 
//     //   contractor_id  : data.contractor_id,
//     //   company_id : data.company_id , 
//     //   category : data.category , 
//     //   id  : data.p_uid
    //      company_name : "ad",
            // message : "message",
            // order_date_time : order_date_time
// }  


export default function Card(props){
    let obj = props.obj 

    let query_obj = {company_img_url : obj.company_img_url, product_img_url : obj.product_img_url, 
        description : obj.description, contractor_id : obj.contractor_id, company_id : obj.company_id,
        category : obj.category, id : obj.p_uid } 

    return (
        <div className= {st.card_container} onClick={() => router.push('/product_pg' , {query : query_obj}) }>
            <div className={st.img}>
                <img src = {obj.product_img_url} /> 
            </div> 

            <div className={st.details} >
                <label htmlFor = "companyname" className="label">
                    Company Name
                </label>
                <div id = "companyname" className="item">
                    {obj.company_name}
                </div>

              

                <label htmlFor = "location" className="label">
                    Location
                </label>
                <div id = "location" className="item">
                    {obj.location}
                </div>

                <label htmlFor = "category" className="label">
                    Category
                </label>
                <div id = "category" className="item">
                    {obj.category} 
                </div>
                
                <label htmlFor = "datetime" className="label">
                    Order Date 
                </label>
                <div id = "datetime" className="item">
                    {obj.order_date_time} 
                </div>

            </div>
        </div>
    )
}