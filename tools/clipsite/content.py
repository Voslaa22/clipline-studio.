"""Copy for every page. Written in the first person: Clipline Studio is one person."""

SITE = "https://cliplinestudio.com"
EMAIL = "cliplines.studio@gmail.com"

HOME = {
    "title": "Clipline Studio · Clipping service for YouTubers, podcasts and streamers",
    "desc": "Clipping service for YouTubers, podcasts and streamers. I cut your long videos into captioned Shorts, TikToks and Reels and post them daily. Get 5 free clips.",
    "og_title": "Clipline Studio: 5 free clips for your channel",
    "og_desc": "Your long videos, cut into daily Shorts, TikToks and Reels. 3M+ views on my own clip accounts in September.",
    "eyebrow": "Sheet 01 · Short-form clipping for YouTubers, podcasts & streamers",
    "h1_pre": "Your long videos, cut into",
    "h1_em": "daily Shorts",
    "h1_post": "that bring viewers back.",
    "sub": "I find the best moments in every episode, cut them vertical with captions and a hook, and post them to TikTok, Instagram Reels and YouTube Shorts on a schedule. You keep filming. I keep your channel in the feed.",
    "cta": "Try it free: 5 clips from your latest video",
    "videos": ["v1", "v2", "v3"],
    "captions": ["hook · 0:15", "reaction", "the story"],
}

CONTENTS = [
    "Vertical 9:16 reframes", "Word-by-word captions", "Hook title in the first second",
    "TikTok", "Instagram Reels", "YouTube Shorts", "Posted on a schedule",
    "Monthly performance report", "You own every file",
]

STEPS = [
    ("Step 1", "You upload as usual", "Every new long video or episode on your channel goes straight into my clipping pipeline. Nothing to send, no extra work."),
    ("Step 2", "I cut the moments", "Hooks, reactions, stories and one-liners are picked, reframed to 9:16, captioned word by word and branded to your channel."),
    ("Step 3", "They go out daily", "Clips are scheduled across TikTok, Reels and Shorts, or delivered as ready-to-post files if you'd rather post yourself."),
]

INCLUDED = [
    "Vertical 9:16 reframe that keeps faces and action in frame",
    "Word-by-word burned-in captions",
    "An on-screen hook title written for the first second",
    "Your handle and branding, subtle and consistent",
    "Captions and hashtags written for each platform",
    "No duplicate or near-duplicate posts",
    "A monthly report: what got views and what to film more of",
    "You own everything. Files are yours to keep.",
]

PLANS = [
    {"key": "starter", "name": "Starter", "price": "$299", "small": "per month · €299",
     "items": ["60 clips a month (2 a day)", "Delivered as ready-to-post files", "Captions + hashtags included", "You post them"],
     "cta": "Start with 5 free clips"},
    {"key": "growth", "name": "Growth", "price": "$499", "small": "per month · €499", "pick": True, "tag": "most popular",
     "items": ["150 clips a month (5 a day)", "I post to TikTok, Reels and Shorts", "Scheduled at your audience's peak times", "Monthly performance report"],
     "cta": "Start with 5 free clips"},
    {"key": "scale", "name": "Scale", "price": "$1,099", "small": "per month · €1,099",
     "items": ["300–360 clips a month (10–12 a day)", "All three platforms, posted for you", "Weekly report + content suggestions", "Priority turnaround on new episodes"],
     "cta": "Start with 5 free clips"},
    {"key": "custom", "name": "Custom", "price": "Let’s talk", "small": "your budget", "custom": True,
     "items": ["Any number of clips", "Your platforms and posting schedule", "Mix clipping and video editing", "Tell me what you need and your budget"],
     "cta": "Send your proposal"},
]

FAQ_HOME = [
    ("Do you post to my accounts, or do I?", "Either. On Growth and Scale I post for you with scheduling access you grant. On Starter I deliver finished files and captions, and you post."),
    ("Who owns the clips?", "You do. They're cut from your videos and delivered to you. I never post your clips anywhere except the accounts you choose."),
    ("How do you pick the moments?", "My pipeline scans the whole video for hooks, reactions, stories and payoffs, then scores them. Each clip must make sense to someone who has never seen your channel."),
    ("What if a video has nothing clip-worthy?", "I'd rather post fewer good clips than padding. Unused clips roll over to the next video."),
    ("Can I cancel?", "Yes, any time. Plans are month to month."),
    ("I have another question", 'Send it through the <a href="#trial">form above</a> or email <a href="mailto:' + EMAIL + '" target="_blank" rel="noopener">' + EMAIL + "</a> and I'll get back to you within 24 hours."),
]

PAGES = [
    {
        "slug": "podcast-clipping",
        "sheet": "02",
        "title": "Podcast Clipping Service · Clipline Studio",
        "desc": "Podcast clipping for video podcasts. I cut every episode into captioned vertical clips for TikTok, Reels and Shorts. Get 5 free clips from your latest episode.",
        "eyebrow": "Sheet 02 · Podcast clipping service",
        "h1_pre": "Every episode, cut into",
        "h1_em": "clips that grow",
        "h1_post": "your podcast.",
        "sub": "I watch the full episode and pull the moments that stand on their own: the hot take, the story, the guest's best line. Each one is reframed to 9:16 on whoever is talking, captioned word by word and posted for you, or sent as ready-to-post files.",
        "cta": "Get 5 free clips from your latest episode",
        "videos": ["d1v", "d2v", "d3v"],
        "captions": ["the hot take", "guest's line", "the story"],
        "why_h": "Why clips work for podcasts",
        "why_lead": "A full episode asks for an hour. A clip asks for 30 seconds, then sends the people who liked it to the full show.",
        "why": [
            ("The best part is buried at minute 52", "Most people will never press play on a 90-minute episode. A clip puts the best moment in front of them first."),
            ("Guest moments travel", "Every strong guest moment is a clip your guest can share with their own audience, which puts your show in front of new listeners."),
            ("One episode, a week of posts", "A long conversation has plenty of standalone moments, so one recording can keep you posting daily until the next episode is out."),
        ],
        "faq": [
            ("Do you clip audio-only podcasts?", "I work from video. If your show is audio-only, email me first and I'll tell you honestly whether clips will work for it."),
            ("How long are the clips?", "Usually 20 to 60 seconds. Each clip is as long as the moment needs to make sense to someone who has never heard your show."),
            ("Can you clip older episodes?", "Yes. Plans count clips, not episodes, so I can pull moments from your back catalogue as well as new episodes."),
            ("Do you post to my accounts, or do I?", "Either. On Growth and Scale I post for you with scheduling access you grant. On Starter I deliver finished files and captions, and you post."),
            ("Who owns the clips?", "You do. They're cut from your episodes and delivered to you. I never post your clips anywhere except the accounts you choose."),
        ],
    },
    {
        "slug": "stream-clipping",
        "sheet": "03",
        "title": "Stream Clipping Service for Twitch, Kick and YouTube Live · Clipline Studio",
        "desc": "Clipping service for streamers. I cut your Twitch, Kick or YouTube Live VODs into captioned vertical clips and post them to TikTok, Reels and Shorts. Get 5 free clips.",
        "eyebrow": "Sheet 03 · Clipping for Twitch, Kick & YouTube Live",
        "h1_pre": "Your stream's best moments,",
        "h1_em": "clipped and posted",
        "h1_post": "for you.",
        "sub": "I go through your VOD and cut the reactions, fails, clutches and chat moments, reframe them to vertical with captions, and post them to TikTok, Reels and Shorts. You stream. I keep you in the feed between streams.",
        "cta": "Get 5 free clips from your last stream",
        "videos": ["v2", "v1", "v3"],
        "captions": ["the clutch", "chat moment", "the fail"],
        "why_h": "Why streamers need clips",
        "why_lead": "Hardly anyone finds a streamer by opening a six-hour VOD. They find a 30-second clip first.",
        "why": [
            ("Nobody rewatches the VOD", "Your best moments happen live and then disappear into hours of footage. Clips give them a second life."),
            ("Clips are how new viewers find you", "A clip reaches people who have never heard of you and gives them a reason to show up next stream."),
            ("Daily posts without the editing", "Consistent clips keep your name in the feed on days you don't stream, and you don't have to touch an editor."),
        ],
        "faq": [
            ("Which platforms do you clip from?", "Twitch, Kick and YouTube Live. If your VOD has a link I can open, I can clip it."),
            ("Do you clip gameplay and IRL streams?", "Both. Send me the stream and I'll pick the moments that work on their own for people who weren't watching live."),
            ("How long are the clips?", "Usually 20 to 60 seconds, long enough for the moment to land and short enough to keep people watching."),
            ("Do you post to my accounts, or do I?", "Either. On Growth and Scale I post for you with scheduling access you grant. On Starter I deliver finished files and captions, and you post."),
            ("Who owns the clips?", "You do. They're cut from your streams and delivered to you. I never post your clips anywhere except the accounts you choose."),
        ],
    },
    {
        "slug": "youtube-clipping",
        "sheet": "04",
        "title": "YouTube Shorts Clipping Service · Clipline Studio",
        "desc": "Turn your long YouTube videos into Shorts, TikToks and Reels. Vertical clips with captions and hooks, posted daily. Get 5 free clips from your latest video.",
        "eyebrow": "Sheet 04 · YouTube Shorts clipping service",
        "h1_pre": "Turn your long videos into",
        "h1_em": "Shorts that send viewers back",
        "h1_post": "to your channel.",
        "sub": "I find the strongest moments in every upload, cut them vertical with a hook title and word-by-word captions, and post them to YouTube Shorts, TikTok and Reels on a schedule. You keep making long videos. I keep your channel in the feed.",
        "cta": "Get 5 free clips from your latest video",
        "videos": ["v1", "v3", "v2"],
        "captions": ["the hook", "the payoff", "the story"],
        "why_h": "Why Shorts work for long-form creators",
        "why_lead": "Shorts are where new viewers sample your channel before they commit to a 20-minute video.",
        "why": [
            ("A front door to your channel", "A good Short shows what your channel is about in seconds and gives people a reason to watch the full video."),
            ("Your back catalogue is full of clips", "Videos you published months ago still have moments that work as Shorts today."),
            ("Daily posts without filming more", "One long video can fill a week of Shorts, so you post every day without adding shoots."),
        ],
        "faq": [
            ("Do you upload Shorts to my channel?", "On Growth and Scale, yes, with access you grant. On Starter I deliver finished files and captions, and you post."),
            ("Can you clip videos that are already out?", "Yes. Plans count clips, not videos, so I can pull moments from older uploads as well as new ones."),
            ("How long are the clips?", "Usually 20 to 60 seconds. Each clip has to make sense to someone who has never seen your channel."),
            ("Who owns the clips?", "You do. They're cut from your videos and delivered to you. I never post your clips anywhere except the accounts you choose."),
            ("Can I cancel?", "Yes, any time. Plans are month to month."),
        ],
    },
]

EDIT = {
    "slug": "video-editing",
    "sheet": "05",
    "title": "Video Editing for YouTubers & Podcasts · Clipline Studio",
    "desc": "Video editing for YouTube videos, podcasts and short-form. Cuts, pacing, captions, sound and colour, delivered ready to upload. Get a free quote within 24 hours.",
    "eyebrow": "Sheet 05 · Video editing service",
    "h1_pre": "Your raw footage, edited into",
    "h1_em": "videos people finish",
    "h1_post": "watching.",
    "sub": "Send me your recording and I send back a finished video, ready to upload: tight cuts, pacing that holds attention, captions, clean sound and colour. For YouTube videos, podcast episodes and short-form.",
    "cta": "Get a free quote",
    "hook": "Car repossessed the week he went all in",
    "caps": [[0, 1, "I was like, all", "right,"], [1, 2, "now I’m locked", "in."], [2, 2.9, "This is", "it."],
             [3, 4, "I’m all", "in."], [4, 5, "I have no other", "option."], [5, 7.2, "There’s no other", "plan."],
             [7.2, 8.1, "Immediately my car", "gets…"]],
    "services": [
        ("YouTube videos", "Your raw footage turned into a finished long-form video: tight cuts, pacing that holds attention, zooms, on-screen text, b-roll, music and sound."),
        ("Podcast episodes", "Full episodes edited for YouTube and Spotify: camera switching, cleaned and levelled audio, intro and outro, and chapters."),
        ("Short-form from raw footage", "TikToks, Reels and Shorts edited from your own clips or footage, with captions, a hook in the first second and fast pacing."),
    ],
    "included": [
        "Cuts that remove pauses, mistakes and dead air",
        "Pacing, zooms and on-screen text that keep people watching",
        "Captions or subtitles, burned in or as a file",
        "Audio cleanup and levelling so every voice is clear",
        "Colour correction for a consistent look",
        "Royalty-free music and sound effects",
        "Revision rounds included in every quote",
        "You own the finished video. Files are yours to keep.",
    ],
    "steps": [
        ("Step 1", "Send your footage", "Share a Drive, Dropbox or WeTransfer link and tell me what you need: length, style and an example you like."),
        ("Step 2", "Get a fixed quote", "Within 24 hours you get a fixed price and delivery date. Nothing starts until you say yes."),
        ("Step 3", "Review and revise", "You get the finished edit, ready to upload. Ask for changes until it's right, within the revision rounds in your quote."),
    ],
    "faq": [
        ("How much does editing cost?", "It depends on the length of the footage and the style you want, so every project gets a fixed quote within 24 hours. You know the full price before any work starts."),
        ("How do I send my footage?", "Upload it to Google Drive, Dropbox or WeTransfer and paste the link in the form. Large files are fine."),
        ("How long does an edit take?", "It depends on the project. Your quote includes a delivery date, and I stick to it."),
        ("Can you match my channel's style?", "Yes. Send a link to a video you like, yours or someone else's, and I'll edit to that style."),
        ("Which languages can you caption?", "English, German, Serbian, Croatian, Bosnian, Macedonian and Russian."),
        ("Who owns the edited video?", "You do. It's your footage and your video, delivered to you to publish wherever you want."),
    ],
}
