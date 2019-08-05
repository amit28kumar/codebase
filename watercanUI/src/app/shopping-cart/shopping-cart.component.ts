import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Globals } from '../globals';

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.css']
})
export class ShoppingCartComponent implements OnInit {

  product_id: any;
  quantity: any;
  result = [];

  constructor(private api: ApiService, private global: Globals) {
    this.getCartDetails();
  }

  getCartDetails = () => {
    if(this.global.specificItemCount.length > 0){
      for(var k in this.global.specificItemCount){
        console.log(this.global.specificItemCount[k].product_id);
        this.product_id = this.global.specificItemCount[k].product_id;
        this.quantity = this.global.specificItemCount[k].count;
        this.api.getProductDetails(this.global.specificItemCount[k].product_id).subscribe(
          data => {
            this.result.push(data[0]);
            if(data[0].id == this.global.specificItemCount[k].product_id){
              console.log(data[0].id);
              console.log(this.global.specificItemCount[k].product_id);
              var res = data[0].price * this.global.specificItemCount[k].count;
              this.global.summation = this.global.summation + res;
            }
          },
          error => {
            console.log(error);
          }
        )
      }
    }
  }

  ngOnInit() {
  }

}
