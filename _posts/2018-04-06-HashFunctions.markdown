---
layout: post
title:  "Hash Functions Quality "
date:   2018-04-06 10:04:36 +0530
categories: Probabilistic_Data_Structures
---
<!-- You’ll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated. -->
<!-- 
To add new posts, simply add a file in the `_posts` directory that follows the convention `YYYY-MM-DD-name-of-post.ext` and includes the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/ -->
Hash functions are magic blocks in solutions for many computational problems. They are used in crypthography, probabilistic data structures(PDS), searching,on average O(1) search capability and many other problems. Different types of problems demand or expect defferent type of qualities from hashfunctions. For example, cryptographic hashfunctions should give different hash values for two different items but hash fucntions used in searching problem are expected to produce same hash values for similar items with high probability. In this article we are interested in non cryptographic hash functions, also known as general purpose hash functions.


Ok, what is hash function?.Any funciton that can be used to map data elements of arbitrary size to data elemnts of fixed size(wiki). Usually hash functions have  some or all below mentioned characteristics,

1. __Determinism__ :  <br/>
A hash procedure must be deterministic - meaning that for a given input value it must always generate the same hash value.

2. __Uniformity__ : <br/>
A good hash function should map the expected inputs as evenly as possible over its output range. That is, every hash value in the output range should be generated with roughly the same probability.

3. __Defined Range:__ <br/>
It is desirable that output of a hash function have fixed size. For example, SHA-1, one of the most widely used cryptographic hash functions produces a 160-bit value.

4. __Data Normalization:__ <br/>
In some applications, the input data may contain features that are irrelevant for comparison purpose. For example, when looking up a personal name, it may be desirable to ignore the distinction between upper and lower case letters.

5. __Continuity:__<br/>
A hash function that is used to search for similar data must be as coninuous as possible; two inputs that differ by a little should be mapped to equal or nearly equal hash values.<br/><br/>Note that continutiy is usally considered a fatal flaw for *checksums, cryptographic hash functions,* and other related concepts.Continutiy is desirable for hash functions only in some applicaitons, such as hash tables used in *Nearest neighbor Search*.

6. __Non-invertible:__<br/>
In cryptographic applications, hash functions are typically expected to be practically non-invertible, 
meaning that it is not realistic to reconstruct the input datum x from its hash value h(x) alone without spending great
amount of time.

In this post we are going to analyze few hash functions with respect to the following parameters.
	
	* uniformity.
	* speed of hash functions- Time taken to compute the hash value.

Uniformity of a hash function can be tested using chi square test. we will explain how to use this test to know the uniformity of a hash function. One main reason to consider the uniformity is many PDS assume that hash functions are uniform. since we are more interested in PDS we consider uniformity.So, We analyse the performance of below hash functions with respect to uniformity and speed.

	1. Murmur Hashes
	2. Crypthographic hash functions like SHA-256
	3. Kirsch-Mitzenmacher-Optimization to only compute 2 instead of k hash functions 
    4. MD5
    5. SHA1
    6. CRC32
    7. Jenkins Hash
    8. one at a time hash
    9. FNV Hash
    10. City Hash

    

