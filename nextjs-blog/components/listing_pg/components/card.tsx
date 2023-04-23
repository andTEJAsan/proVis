import React from "react" 
import st from "../../../styles/listing_pg/card.module.css"
import { alertService } from "../../../services/alert.service"  ;
import { useDispatch, useSelector } from "react-redux";
import {RootState} from "../../../redux/reducers"
import config from "config"; 


export default function Card(props) { 
    

    const { isLoggedIn} = useSelector(
        (state: RootState) => state.storage
      );
    let obj = props.obj 
    let [bookmark_url, set_bookmark_url] = React.useState("/listing_pg/bookmark.png")  

    async function  bookmark_handler() {
        const { apiUrl } = config;
        if (!isLoggedIn) {
            alertService.error('Please Login First!!', {autoClose : true})
            return 
        }
        else {
            const queryid = useSelector((state : RootState) => state.storage.userID)

            const request_obj = {
                "cus_uid" : queryid , 
                "p_uid" : props.id  
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
                
    //     <Link href={"/about"} passHref>
    //     <div className={st.dropbtn}><p className={st.navText}>{"About Us"}</p></div>
    //   </Link>
                
                <div className= {st.card_container} >
                    <img src = {obj.product_img_url} className= {st.card_img1} />
                    
                    <div className= {st.details1} >
                        <img src = {obj.company_img_url} className= {st.card_img2} />
                        <div className= {st.contractor_div} >
                            <div className={st.contractor}>
                                {obj.contractor_name} 
                            </div>
                            
                        </div>
                        <button className= {st.btn} onClick={props.clicker}>Connect</button>
                        <img src = {bookmark_url} onClick = {bookmark_handler} />  
                </div>
                    <div className={st.details2}>
                        {obj.description}
                    </div>
                </div>
    )
} 