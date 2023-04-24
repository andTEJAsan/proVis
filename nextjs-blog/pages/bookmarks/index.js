import React from "react";
import PageTemplate from "../../components/reusable/template/PageTemplate.tsx";
import Card from "../../components/listing_pg/components/card.tsx";
import Spinner from "../../components/authModal/components/spinner";
import st from "../../styles/listing_pg/card.module.css";

export default function Bookmarks() {
  let [newState, SetState] = React.useState({ location: "", category: "" });
  let [cardsState, setCardsState] = React.useState([]);
  let [loader, setLoader] = React.useState(true);

  let new_card_array = [];

  //   useEffect(() => {
  //     console.log("product fetch");
  //     let url_fetch = `${apiUrl}/api/products/findByTags`;
  //     let loc_fetch = `?location=${newState.location}`;
  //     let cat_fetch = `&category=${newState.category}`;

  //     if (newState.location == "") {
  //       loc_fetch = "";
  //       cat_fetch = "?" + cat_fetch;
  //     }

  //     if (newState.category == "") {
  //       cat_fetch = "";
  //     }
  //     url_fetch = url_fetch + loc_fetch + cat_fetch;

  //     fetch(url_fetch, {
  //       method: "GET",
  //       headers: {
  //         "Content-Type": "application/json",
  //         // Authorization: `Bearer ${jwt}`,
  //       },
  //     })
  //       .then((response) =>
  //         response.json().then((data) => {
  //           console.log("printing data");
  //           console.log(data);
  //           console.log("entered json method");
  //           function gen_obj(data) {
  //             let id = data.p_uid;
  //             let location = data.location;
  //             let category = data.category;
  //             let product_img_url = data.product_img_url;
  //             let description = data.product_description;
  //             let company_name = data.company_name;
  //             let company_img_url = data.company_img_url;
  //             let contractor_id = data.contractor_id;
  //             let contractor_name = data.contractor_name;

  //             let obj = {
  //               id,
  //               location,
  //               category,
  //               product_img_url,
  //               description,
  //               company_name,
  //               company_img_url,
  //               contractor_id,
  //               contractor_name,
  //             };
  //             return obj;
  //           }

  //           function gen_query(data_arr) {
  //             return data_arr.map((x) => ({
  //               company_img_url: x.company_img_url,
  //               product_img_url: x.product_img_url,
  //               description: x.description,
  //               contractor_name: x.contractor_name,
  //               category: x.category,
  //               id: x.p_uid,
  //               company_id: x.company_id,
  //               contractor_id: x.contractor_id,
  //             }));
  //           }
  //           let query_arr = gen_query(data);
  //           console.log("query_arr");
  //           console.log(query_arr);

  //           for (let i = 0; i < data.length; i++) {
  //             new_card_array.push(
  //               <Card
  //                 clicker={() =>
  //                   router.push({ pathname: "/product_pg", query: query_arr[i] })
  //                 }
  //                 obj={gen_obj(data[i])}
  //                 key={data[i].p_uid}
  //               />
  //             );
  //           }

  //           if (new_card_array.length == 0) {
  //             new_card_array.push(<div>No data to show!</div>);
  //           }
  //           setLoader(false);
  //           setCardsState(new_card_array);
  //         })
  //       )
  //       .catch((err) => {
  //         setLoader(false);
  //         new_card_array.push(
  //           <div
  //             style={{
  //               width: "700px",
  //               justifyContent: "center",
  //               display: "flex",
  //             }}
  //           >
  //             No data to show!
  //           </div>
  //         );

  //         setCardsState(new_card_array);
  //       });
  //   }, []);

  return (
    <PageTemplate outsideApp>
      <div className={st.cards}>
        {loader == true ? <Spinner /> : cardsState}
      </div>
    </PageTemplate>
  );
}
