
import React , {useEffect} from "react";
import { useRouter } from 'next/router'
import config from "../../config" 
import PageTemplate from "@components/reusable/template/PageTemplate.tsx";
import Navbar from "./components/navbar"
import Listing_Box  from "./components/listing_box";
import Card  from "./components/card";
import products from "./data/products"
import Dropdown from "./components/dropdown"
import st from "../../styles/listing_pg/app.module.css"
// import cross from "../../public/listing_pg/cross.png" 
        // {
//   "p_uid": "vycs78",
//   "location": "Delhi",
//   "category": "interior design",
//   "product_img_url": "https://www.youtube.com/",
//   "product_description": "this is the worst",
//   "company_name": "proVis",
//   "company_img_url": "https://www.youtube.com/",
//   "contractor_id": "82390kf"
// }


function App() {
  let router = useRouter() 
  // let card_array = products.map((obj) => <Card obj = {obj} key = {obj.id} />)
  // let arr = ["aaveg","arnav"]

  // let [newLocation,setLocationState] = React.useState("Delhi")  
  // let [newCategory,setCategoryState] = React.useState("Interior Designers & Decorators") 

  let [newState, SetState] = React.useState({location : "", category : ""}) 
  let [cardsState, setCardsState] = React.useState([]) 

  let cross = "/listing_pg/cross.png" 

  let {apiUrl} = config
  

  function locationHandler(location){
   
    SetState((prevState) => {
      return { ...prevState, 
          location : location
    }
  }) 
  }

  function categoryHandler(category){
    SetState((prevState) => {
      return { ...prevState, 
          category : category
    }
  }) 
  }

  function remove_category() { 
    SetState((prevState) => {
      return { ...prevState, 
          category : ""
    }
  }) 
  }

  function remove_location() { 
    SetState((prevState) => {
      return { ...prevState, 
          location : ""
    }
  }) 
  }

  
useEffect(() => {
  fetch(`${apiUrl}/api/products?location=${newState.location}&category=${newState.category}` , {
    method : 'GET', 
      headers: {
        "Content-Type": "application/json" 
          // Authorization: `Bearer ${jwt}`,
      }
  }).then(response =>
    response.json().then(data => {
      function gen_obj(data){
        let id = data.p_uid 
        let location = data.location
        let category = data.category
        let product_img_url = data.product_img_url
        let description = data.product_description 
        let company_name = data.company_name 
        let company_img_url = data.company_img_url
        let contractor_id = data.contractor_id 
        let contractor_name = data.contractor_name
         
        let obj = {id,location,category,product_img_url,description, company_name,company_img_url, contractor_id,contractor_name} 
        return obj 
      }
      let query_obj = {company_img_url : data.company_img_url , 
                        product_img_url : data.product_img_url,
                        description : data.description , 
                        contractor_name  : data.contractor_name, 
                        category : data.category , 
                        id  : data.p_uid}  
      let new_card_array = data.map((obj) => <Card clicker = {() => router.push('/product_pg' , {query : query_obj}) }
                                                   obj = {gen_obj(obj)} key = {obj.p_uid} />)
      setCardsState(new_card_array) 
    })
  ).catch((err) => console.error(err));
}, [newState]);
 


let [locationarr, setlocationarr] = React.useState(["Delhi","New Delhi", "South Delhi", "West Delhi"] ) 
let [categoryarr, setcategoryarr] = React.useState(["Interior Designers & Decorators", "Architects & Building Designers", "Civil Engineers & Contractors",
                                                    "Design-Build Firms"] ) 
useEffect(() => {
    fetch(`${apiUrl}/api/locations` , {
      method : 'GET', 
        headers: {
          "Content-Type": "application/json" 
            // Authorization: `Bearer ${jwt}`,
        }
    }).
    then((res) => res.json().then(
      (data) => {
                  let newlocations = data.map(x => x.name) 
                  setlocationarr(newlocations) 
                }
    ) ).
    catch((err) => console.log(err))
    }, []) ; 

  
  useEffect(() => {
    fetch(`${apiUrl}/api/categories` , {
      method : 'GET', 
        headers: {
          "Content-Type": "application/json" 
            // Authorization: `Bearer ${jwt}`,
        }
    }).
    then((res) => res.json().then(
      (data) => {
                  let newcategories = data.map(x => x.name) 
                  setcategoryarr(newcategories) 
                }
    ) ).
    catch((err) => console.log(err))
    }, []) ; 

 
  return (
    <PageTemplate transparentNav={false} outsideApp darkBg={true} noFilter>
   <div>
    <Listing_Box/>
    <div className = {st.container}>
        <div className={st.search_bars}>
                        <div className={st.location}>
                          <h3>Location</h3>
                          <Dropdown 
                                  trigger_text = "Select Location" 
                                  values = {locationarr} 
                                  f = { locationHandler }
                          />
                        </div>
                        <div className={st.category}>
                          <h3>Category</h3>
                          <Dropdown 
                                  trigger_text = "Select Category" 
                                  values = {categoryarr}
                                  f = { categoryHandler }
                          />
                        </div>
        </div>
                    
        <div className={st.display_tags} >
            { (newState.location !== "" ) && <div className={st.tag} >{newState.location} 
                                                              <button className={st.tag_button} onClick={remove_location}><img src ={cross} className={st.img_button} /></button>      
                                                        </div>} 
            { (newState.category !== "") && <div className={st.tag}>{newState.category} 
                                                              <button className={st.tag_button} onClick={remove_category}><img src ={cross} className={st.img_button} /></button>
                                                        </div>}
        </div>
        <div className= {st.cards}>{cardsState}</div>
     
   </div>
  </div>

</PageTemplate>
  );

  
 
}

export default App;
