import React, { useEffect } from "react" 
import { useSelector } from "react-redux";
import { RootState } from "../../redux/reducers"
import config from "../../config";
import Order from "./components/order"
import PageTemplate from "@components/reusable/template/PageTemplate";
import st from "../../styles/dashboard/app.module.css" 
import { Card, Space } from 'antd';

export default function App(){
    let obj  = {
        company_img_url : "", 
        product_img_url : "", description : "", company_name : "", location : "", category : "", order_date_time : "",
        company_id :"", p_uid : ""
    }
    let com_img_url  = "https://img.freepik.com/free-photo/blue-house-with-blue-roof-sky-background_1340-25953.jpg"
    let prod_img_url = "https://img.freepik.com/free-photo/blue-house-with-blue-roof-sky-background_1340-25953.jpg"
    let desc = "Perhaps duty is the death of love" 
    let com_name = "Watson and Holmes" 
    let loc = "Noida" ; let cat = "Interior Design " ;
    let date_time = "19/04/2003" 

    obj.company_img_url = com_img_url ; obj.product_img_url = prod_img_url ; obj.description = desc ; 
    obj.company_name = com_name ; obj.location = loc ; obj.category  = cat ; obj.order_date_time = date_time ; 
    obj.company_id = "1" ; obj.p_uid = "1" ; 

    const id = useSelector((state : RootState) => state.storage.userID)
    // get user id from state
    let [userState, setUserState] = React.useState({name : "", emailid: "", phone_number : ""})

    let [orderState, setOrderState] = React.useState([]) 

    function genarr(data){
        return data.map((x) => <Order obj = {x} /> ) 
    }

    const { apiUrl } = config;
    let temp_arr = [] 
    for (let i = 0 ; i  < 10 ; i ++){
        temp_arr.push(<Order obj = {obj} />) 
    }
    useEffect(() => {
        setOrderState(temp_arr) 
    }, [orderState])  

//     useEffect(() => {
//         Promise.all([ fetch(`${apiUrl}/api/customers/${id}` , {
//             method : 'GET', 
//               headers: {
//                 "Content-Type": "application/json" 
//                   // Authorization: `Bearer ${jwt}`,
//               }
//     }), fetch(`${apiUrl}/api/customers/${id}/orders`, {
//         method : "GET",
//         headers : {
//             "Content-Type": "application/json" 
//         }
// })])

//     .then(([cus_response, order_response]) => Promise.all([cus_response.json(),order_response.json()])
//     .then(([customer_data,order_data]) => {
//         setUserState({name : customer_data.name, emailid : customer_data.emailid, phone_number: customer_data.phone_number})
//         setOrderState(genarr(order_data))
//         console.log("printing order_data") 
//         console.log(genarr(order_data))
//     }
//     )).catch((err) => console.error(err))
//     }, []) 


   
      



    let dashboard_url = "https://img.freepik.com/free-photo/brown-wooden-flooring_53876-90802.jpg?w=996&t=st=1680938897~exp=1680939497~hmac=d5bfaf1218dcd7b4c1c96e2696088de57dc236aa8f4fb73e46df65a56e51fda8" 
    return (
        <PageTemplate transparentNav={false} outsideApp darkBg={true} noFilter>
            <div className= {st.header}>
                    <img src = {dashboard_url} className={st.dashboard_img} />
           </div>
        <div className={st.detailscontainer}>
                <Space direction="vertical" size={16} className={st.space}>
                    
                    <Card title="User Dashboard"  style={{ width: 400 , height : 200}} className={st.card}>
                    
                    {/* <p><strong>Name</strong> <span className={st.label}>{userState.name}</span> </p>
                    <p><strong>Phone Number</strong><span className={st.label}>{userState.phone_number}</span> </p>
                    <p><strong>Email Address</strong><span className={st.label}> {userState.emailid} </span></p> */}

                    <p><strong>Name</strong> <span className={st.label}>Aaveg Jain</span> </p>
                    <p><strong>Phone Number</strong><span className={st.label}>9205231951</span> </p>
                    <p><strong>Email Address</strong><span className={st.label}>aavegj1904@gmail.com</span></p>

                    </Card>

                    {/* <Card size="small" title="Small size card" extra={<a href="#">More</a>} style={{ width: 300 }}>
                    <p>Card content</p>
                    <p>Card content</p>
                    <p>Card content</p>
                    </Card> */}
                </Space>
            <div className={st.orderdetails} >
                <div className={st.ordertext}>Your Orders</div>
                {orderState} 
            </div>
        </div>
    </PageTemplate>
    )

}




// <div className="container">
                // <div className= {st.header}>
                //     <img src = {dashboard_url} className={st.dashboard_img} />
                // </div>

//                 <div className="user_details">
//                     <h3>User Details</h3>
//                     {/* <h5><button>Edit profile</button></h5> */}
//                     <div className="details">
//                         <label htmlFor = "name" className="label">Name</label>
//                         <p id = "name" className="info">{userState.name}</p>
//                         {/* {userState.name} {userState.emailid} */}
//                         <label htmlFor = "email" className="label">Email</label>
//                         <p id = "email" className="info">{userState.emailid}</p>
//                         <label htmlFor = "phoneno" className="label">Phone Number</label>
//                         <p id = "email" className="info">{userState.phone_no}</p>
//                     </div>
//                 </div>

//                 <div className="order_details">
//                     {orderState} 
//                 </div>

//             </div>