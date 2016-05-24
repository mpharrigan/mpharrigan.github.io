---
title: Making ffmpeg work
excerpt: |+
    When you have proteins in space evolving over time, you have to make a
    movie. VMD is a love-hate program that is very capable of nice renders of
    biophysical systems.  I like to have more control over the transformation
    of each rendered frame into a movie file.

    `ffmpeg` is a command-line program that can do this. If you try with the
    default options, your movie will have lots of compression scarring and may
    not play in most contexts.
---

<figure class="figure">
<video width="100%" controls>
    <source src="https://www.dropbox.com/s/j36tdxqcwv1k5yl/nav.ionpull.slow.small.mp4?dl=1" type="video/mp4">
Your browser does not support the video tag.
</video>
<figcaption class="figure-caption" markdown="1">
To learn how to make this video, read on!
(Except I scaled this down for web; [full resolution][original])
</figcaption>
</figure>

When you have proteins in space evolving over time, you have to make a
movie. [VMD] is a love-hate program that is very capable of nice renders of
biophysical systems.  I like to have more control over the transformation
of each rendered frame into a movie file.

`ffmpeg` is a command-line program that can do this. If you try with the
default options, your movie will have lots of compression scarring and may
not play in most contexts.

[VMD]: http://www.ks.uiuc.edu/Research/vmd/

### Getting `ffmpeg`

There are some confusing politics with `ffmpeg` being forked into `avconv`
and that getting picked up by debian-based distros, but then they were
meanies so you shouldn't use it (???). The safest thing is to [get the
latest version][ffmpeg] of `ffmpeg` and build from source.

{: .language-bash}
    aptitude install libx264-dev
    ./configure --enable-libx264 --enable-gpl

[ffmpeg]: https://www.ffmpeg.org/

### Good quality movie from individual frames

{: .language-bash}
    ffmpeg \
        -framerate 24 -i frames/final.protein.%05d.tga \
        -c:v libx264 \
        -preset slow \
        -crf 18 \
        -r 24 \
        movie.mp4

This will make a movie from VMD frames. You can change the filename format
string (`%05d` means zero-padded integers to width 5 (default from VMD)).
The file indices have to be contiguous.

`-framerate 24`
:   You can change this to speed up or slow down your movie. The output
    framerate is given by the `-r` option.

`-c:v libx264`
:   Use H.264 to encode your movie. This is a good, well-supported encoding
    that seems to be everyone's favorite.

`-preset slow`
:   Try hard to reduce the file size. It's not that slow.

`-crf 18`
:   "Quality". This means essentially lossless. Higher is worse.
    ffmpeg documentation
    [here](https://www.ffmpeg.org/ffmpeg-codecs.html#toc-Options-23)
    and explanation [here](http://slhck.info/articles/crf).

`-r 24`
:   Output frame rate. If you are speeding up your rendered frames with
    `-framerate` > 24, make sure you set this or your movie will look
    jittery in Powerpoint.

### Stack two movies side-by-side

I'll often want two rotations of a protein both shown in a movie. You can
stack them side by side using the at-first-intimidating-but-then-not-so-bad
"filter language" in `ffmpeg`


{: .language-bash}
    ffmpeg \
        -framerate 24 -i frames/final.frontview.%05d.tga \
        -framerate 24 -i frames/final.sideview.%05d.tga \
        -c:v libx264 \
        -preset slow \
        -crf 18
        -filter_complex "[0:v][1:v] hstack"
        -r 24 movie.mp4

This is the important line

{: .language-bash}
        -filter_complex "[0:v][1:v] hstack"

The general form of this language is `inputs command output`. Here, our
inputs are the 0th and 1st video streams. The command is `hstack`, which
stacks two streams horizontally. The implicit output is the final movie.

### Stack and overlay

Using your favorite plotting software, you can make an animated plot by
saving a bunch of frames with zero-padded indices in the filename. Add it
as another `-i` option. Now you can hstack and overlay your plot.

{: .language-bash}
    -filter_complex "\
        [0:v][1:v] hstack [stacked] ;\
        [stacked][2:v] overlay=eval='init':x=W/2-w/2:y=H/2-h/2"

Now the output of `hstack` is a stream named `stacked`. It's used as input
for the second command, along with the 2nd video stream (our plot frames).
The command here is `overlay`. It takes some parameters.

`eval='init'`
:   Compute x and y only once. This means our overlay doesn't move around.

`x=W/2-w/2`
:   The x position is given in terms of the base video's width (`W`) and
    the overlay's width (`w`). This centers the overlay.

The parameters are of the form `key=value` and delimited with `:`. The
implicit output is once again our output.


### Stack, overlay, reverse

This does the above and then shows the movie in reverse.

{: .language-bash}
    ffmpeg \
        -framerate 40 -i frames/final.side.%05d.tga \
        -framerate 40 -i frames/final.bottom.%05d.tga \
        -framerate 40 -i frames/plot.%05d.png \
        -c:v libx264 \
        -preset slow \
        -crf 18 \
        -filter_complex "\
                [0:v][1:v] hstack [stacked] ;\
                [stacked][2:v] overlay=eval='init':x=W/2-w/2:y=H/2-h/2 [layed] ;\
                [layed] split [layed1][layed2] ;\
                [layed2] reverse [revved] ;\
                [layed1][revved] concat" \
        -r 24 nav.ionpull.slow.small.mp4

The movie at the top of this page was scaled using `[catted]
scale=w=1024:h=-1"` and saved with `-crf 23` (slightly worse) for a 2.3 MiB
file. The [original] is 28 MiB.

[original]: https://www.dropbox.com/s/1lzuew0ngfhptjf/nav.ionpull.slow.mp4?dl=1
