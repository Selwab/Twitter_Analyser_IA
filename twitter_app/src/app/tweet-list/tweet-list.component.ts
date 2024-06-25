import { CommonModule} from '@angular/common';
import { Component, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Tweet } from '../interfaces/tweet';
import { TweetComponent } from '../tweet/tweet.component';

@Component({
  selector: 'app-tweet-list',
  standalone: true,
  imports: [FormsModule, CommonModule, TweetComponent],
  templateUrl: './tweet-list.component.html',
  styleUrl: './tweet-list.component.css'
})
export class TweetListComponent {
  @Input() tweetsList!: Tweet[];
}
