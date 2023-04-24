import React from "react" 
import st from "../../../styles/listing_pg/card.module.css"
import { alertService } from "../../../services/alert.service"  ;
import { useDispatch, useSelector } from "react-redux";
import {RootState} from "../../../redux/reducers"
import config from "config"; 


export default function Card(props) { 
    
    console.log(props) 
    const { isLoggedIn} = useSelector(
        (state: RootState) => state.storage
      );
    let obj = props.obj 
    // obj.description = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged"
    let [bookmark_url, set_bookmark_url] = React.useState("/listing_pg/bookmark.png")  
    const queryid = useSelector((state : RootState) => state.storage.userID)

    async function  bookmark_handler() {
        const { apiUrl } = config;
        if (!isLoggedIn) {
            alertService.error('Please Login First!!', {autoClose : true})
            return 
        }
        else {
            

            const request_obj = {
                "cus_uid" : queryid.toString() , 
                "p_uid" : props.obj.id.toString()   
            }
            const response = await fetch(`${apiUrl}/api/customers/${queryid}/bookmarks`, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json"
                },
                body: JSON.stringify(request_obj)  
              } ) ;
            
              if (response.ok) {
                alertService.success('Bookmarked', {autoClose : true})
                set_bookmark_url("/listing_pg/yellow_bookmark.png") 

              } 
              else console.log(response) 
    }
    }
    return (
                

                
                <div className= {st.card_container} >
                    <img src = {obj.product_img_url} className= {st.card_img1} />
                    
                    <div className= {st.details1} >
                        <img src = {obj.company_img_url} className= {st.card_img2} />
                        <div className= {st.contractor_div} >
                            <div className={st.contractor}>
                                {obj.contractor_name} 
                            </div>
                            
                                <img className={st.bookmarkimg} src = {bookmark_url} onClick = {bookmark_handler} />
                            
                        </div>
                        <button className= {st.btn} onClick={props.clicker}>
                            <div className={st.btntext}>Connect</div>
                        </button>
                          
                </div>
                    <div className={st.details2}>
                        {obj.description}
                    </div>
                </div>
    )
} 