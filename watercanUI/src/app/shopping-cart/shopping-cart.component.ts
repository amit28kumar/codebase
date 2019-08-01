import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Globals } from '../globals';

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.css']
})
export class ShoppingCartComponent implements OnInit {

  constructor(private api: ApiService, private global: Globals) {
    this.getCartDetails();
  }

  getCartDetails = () => {
    var data = localStorage.getItem("item")
    console.log(data);
    console.log(data.product);
  }

  ngOnInit() {
  }

}
