import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Globals } from '../globals';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  product_details: any;
  filtered_product = [];

  constructor(private api: ApiService, private global: Globals) {
    this.getProductDetails();
    // this.getFilteredProducts();
  }

  getProductDetails = () => {
    this.api.getProductDetails().subscribe(
      data => {
        this.product_details = data;
      },
      error => {
        console.log(error);
      }
    )
  }

  getFilteredProducts = () => {
    this.filtered_product = []
    for(var k in this.product_details){
      if(this.product_details[k].product.replace(/ /g,'').toLowerCase() == this.global.searchKey.toString().toLowerCase()){
        this.filtered_product.push(this.product_details[k])
      }
      else if(this.product_details[k].product.replace(/ /g,'').toLowerCase().includes(this.global.searchKey.toString().toLowerCase())){
        this.filtered_product.push(this.product_details[k])
      }
      else if(this.product_details[k].category.replace(/ /g,'').toLowerCase().includes(this.global.searchKey.toString().toLowerCase())){
        this.filtered_product.push(this.product_details[k]);
      }
    }
    console.log(this.filtered_product);
    return this.filtered_product;
  }

  setSearchFlag(){
    this.global.searchKey != this.global.searchKey;
  }

  addToCart = (product) =>{
    console.log(product);
    if(product){
      this.global.itemCount = parseInt(this.global.itemCount) + 1;
      console.log(this.global.itemCount);
      // localStorage.setItem("cartItemCount",this.global.itemCount);
      // console.log(localStorage);
    }
  }

  ngOnInit() {
  }

}
