import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Globals } from '../globals';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  products: any;
  product_details: any;
  cartObject = {"product" : 0, "count" : 0};
  constructor(private api: ApiService, private global: Globals) {
    this.getProduct();
    this.getProductDetails();
  }

  getProduct = () => {
    this.api.getProduct().subscribe(
      data => {
        this.products = data
      },
      error => {
        console.log(error);
      }
    )
  }

  getProductDetails = () => {
    this.api.getProductDetails().subscribe(
      data => {
        this.product_details = data
      },
      error => {
        console.log(error);
      }
    )
  }

  count(name){
    var data = []
    for(var k in this.product_details){
      if(this.product_details[k].product == name){
        data.push(this.product_details[k]);
      }
    }
    return data.length;
  }

  addToCart = (product) =>{
    console.log(product);
    var product_id = product.id;
    var flag = false;
    // this.global.dict = {}
    if(product_id){
      this.global.itemCount = parseInt(this.global.itemCount) + 1
      if(this.global.specificItemCount.length == 0){
        this.global.dict['product_id'] = product_id;
        this.global.dict['count'] = 1;
        this.global.specificItemCount.push(this.global.dict);
        this.global.dict = {}
      }
      else{
          for(var k in this.global.specificItemCount){
            if(this.global.specificItemCount[k].product_id == product_id){
              this.global.specificItemCount[k].count = this.global.specificItemCount[k].count + 1;
              flag = true;
              this.global.dict = {}
            }
          }
          if(!flag){
            this.global.dict['product_id'] = product_id;
            this.global.dict['count'] = 1;
            this.global.specificItemCount.push(this.global.dict);
            this.global.dict = {}
          }
      }

      console.log(this.global.specificItemCount);
    }
  }

  getSearchFlag = () => {
    return this.global.searchFlag;
  }

  setSearchFlag = () => {
    if(this.global.searchFlag){
      this.global.searchFlag = !this.global.searchFlag;
    }
  }

  ngOnInit() {
    // localStorage.setItem("item",JSON.stringify(this.cartObject));
  }

}
