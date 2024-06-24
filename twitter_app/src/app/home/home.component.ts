import { Component, viewChild } from '@angular/core';
import { FormsModule, NgModel }   from '@angular/forms';
import { Tweet } from '../interfaces/tweet';
import { CommonModule } from '@angular/common';
import { TweetComponent } from '../tweet/tweet.component';
import { TweetListComponent } from '../tweet-list/tweet-list.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule, CommonModule, TweetComponent, TweetListComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  tweetsList: Tweet[] = [];
  tweetContent: string = '';
  contentInput: string = '';

  postTweet() {
    const newTweet: Tweet = {
      code: 1,
      content: this.contentInput,
      sentimentID: 0,
      imageURL: '',
      hour: new Date(),
      date: new Date()
    }
    this.tweetsList.push(newTweet);
    this.tweetContent = this.contentInput;
    this.contentInput = '';
    console.log("Posted Tweets: ", newTweet);
  }
}
