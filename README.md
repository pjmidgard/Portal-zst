# Portal4.py

Speed: Ultra 2KB - 2MB Max 10MB - 10 GB/s

Add instructions:

cl, cld, cld3 ; cldd3, cldd, ul

cld, cld3; cldd3 cld

cld, cld3, cld, cld3; cldd3, cldd, cldd3, cldd

cl; ul;

Jurijus Pacalovas written program.

4.19 v. zst

0%-99.8535% c.

Cryptography

zst

Lossless compression

From MySQL Shell 8.0.20, for X Protocol connections and classic MySQL protocol connections, whenever you create a session object to manage a connection to a MySQL Server instance, you can specify whether compression is required, preferred, or disabled for that connection. • required requests a compressed connection from the server, and the connection fails if the server does not support compression or cannot agree with MySQL Shell on a compression protocol. • preferred requests a compressed connection from the server, and falls back to an uncompressed connection if if the server does not support compression or cannot agree with MySQL Shell on a compression protocol. This is the default for X Protocol connections. • disabled requests an uncompressed connection, and the connection fails if the server only permits compressed connections. This is the default for classic MySQL protocol connections. From MySQL Shell 8.0.20, you can also choose which compression algorithms are allowed for the connection. By default, MySQL Shell proposes the zlib, LZ4, and zstd algorithms to the server for X Protocol connections, and the zlib and zstd algorithms for classic MySQL protocol connections (which do not support the LZ4 algorithm). You can specify any combination of these algorithms. The order in which you specify the compression algorithms is the order of preference in which MySQL Shell proposes them, but the server might not be influenced by this preference, depending on the protocol and the server configuration. Specifying any compression algorithm or combination of them automatically requests compression for the connection, so you can do that instead of using a separate parameter to specify whether compression is required, preferred, or disabled. With this method of connection compression control, you indicate whether compression is required or preferred by adding the option uncompressed (which allows uncompressed connections) to the list of compression algorithms. If you do include uncompressed, compression is preferred, and if you do not include it, compression is required. You can also pass in uncompressed on its own to specify that compression is disabled. If you specify in a separate parameter that compression is required, preferred, or disabled, this takes precedence over using uncompressed in the list of compression algorithms. You can also specify a numeric compression level for the connection, which applies to any compression algorithm for X Protocol connections, or to the zstd algorithm only on classic MySQL protocol connections. For X Protocol connections, if the specified compression level is not acceptable to the server for the algorithm that is eventually selected, the server chooses an appropriate setting according to the behaviors listed in Connection Compression with X Plugin. For example, if MySQL Shell requests a compression level of 7 for the zlib algorithm, and the server's mysqlx_deflate_max_client_compression_level system variable (which limits the maximum compression level for deflate, or zlib, compression) is set to the default of 5, the server uses the highest permitted compression level of 5. If the MySQL server instance does not support connection compression for the protocol (which is the case before MySQL 8.0.19 for X Protocol connections), or if it supports connection compression but does not support specifying connection algorithms and a compression level, MySQL Shell establishes the connection without specifying the unsupported parameters. To request compression for a connection from MySQL Shell 8.0.20, use one of the following methods: • If you are starting MySQL Shell from the command line and specifying connection parameters using separate command options, use the --compress (-C) option, specifying whether compression is required, preferred, or disabled for the connection. For example: shell> mysqlsh --mysqlx -u user -h localhost -C required

The --compress (-C) option is compatible with earlier releases of MySQL Shell (back to MySQL 8.0.14) and still accepts the boolean settings from those releases. From MySQL Shell 8.0.20, if you specify just --compress (-C) without a parameter, compression is required for the connection. The above example for an X Protocol connection proposes the zlib, LZ4, and zstd algorithms to the server in that order of preference. If you prefer an alternative combination of compression algorithms, you can specify this by using the --compression-algorithms option to specify a string with a comma-separated list of permitted algorithms. For X Protocol connections, you can use zlib, lz4, and zstd in any combination and order of preference. For classic MySQL protocol connections, you can use zlib and zstd in any combination and order of preference. The following example for a classic MySQL protocol connection allows only the zstd algorithm: shell> mysqlsh --mysql -u user -h localhost -C preferred --compression-algorithms=zstd You can also use just --compression-algorithms without the --compress (-C) option to request compression. In this case, add uncompressed to the list of algorithms if you want to allow uncompressed connections, or omit it if you do not want to allow them. This style of connection compression control is compatible with other MySQL clients such as mysql and mysqlbinlog. The following example for a classic MySQL protocol connection has the same effect as the example above where preferred is specified as a separate option, that is, to propose compression with the zstd algorithm but fall back to an uncompressed connection: shell> mysqlsh --mysql -u user -h localhost --compression-algorithms=zstd,uncompressed You can configure the compression level using the --compression-level or --zstd- compression-level options, which are validated for classic MySQL protocol connections, but not for X Protocol connections. --compression-level specifies an integer for the compression level for any algorithm for X Protocol connections, or for the zstd algorithm only on classic MySQL protocol connections. --zstd-compression-level specifies an integer from 1 to 22 for the compression level for the zstd algorithm, and is compatible with other MySQL clients such as mysql and mysqlbinlog. For example, these connection parameters for an X Protocol connection specify that compression is required for the global session and must use the LZ4 or zstd algorithm, with a requested compression level of 5: shell> mysqlsh --mysqlx -u user -h localhost -C required --compression-algorithms=lz4,zstd --compression-level=5 • If you are using a URI-like connection string to specify connection parameters, either from the command line, or with MySQL Shell's \connect command, or with the shell.connect(), shell.openSession(), mysqlx.getSession(), mysql.getSession(), or mysql.getClassicSession() function, use the compression parameter in the query string to specify whether compression is required, preferred, or disabled. For example: mysql-js> \connect user@example.com?compression=preferred shell> mysqlsh mysqlx://user@localhost:33060?compression=disabled Select compression algorithms using the compression-algorithms parameter, and a compression level using the compression-level parameter, as for the command line options. (There is no zstd-specific compression level parameter for a URI-like connection string.) You can also use the compression-algorithms parameter without the compression parameter, including or omitting the uncompressed option to allow or disallow uncompressed connections. For example, both these sets of connection parameters specify that compression is preferred but uncompressed connections are allowed, the zlib and zstd algorithms are acceptable, and a compression level of 4 should be used: mysql-js> \connect user@example.com:33060?compression=preferred&compression-algorithms=zlib,zstd&compression-level=4 mysql-js> \connect user@example.com:33060?compression-algorithms=zlib,zstd,uncompressed&compression-level=4 • If you are using key-value pairs to specify connection parameters, either with MySQL Shell's \connect command or with the shell.connect(), shell.openSessio

mysqlx.getSession(), mysql.getSession(), or mysql.getClassicSession() function, use the compression parameter in the dictionary of options to specify whether compression is required, preferred, or disabled. For example: mysql-js> var s1=mysqlx.getSession({host: 'localhost', user: 'root', password: 'password', compression: 'required'}); Select compression algorithms using the compression-algorithms parameter, and a compression level using the compression-level parameter, as for the command line and URI- like connection string methods. (There is no zstd-specific compression level parameter for key-value pairs.) You can also use the compression-algorithms parameter without the compression parameter, including or omitting the uncompressed option to allow or disallow uncompressed connections and zeroes and ones.

Zstandard combines a dictionary-matching stage (LZ77) with a large search window and a fast entropy coding stage, using both Finite State 
Entropy (a fast tabled version of ANS, tANS, used for entries in the Sequences section), and Huffman coding (used for entries in the Literals section).

LZ77 algorithms achieve compression by replacing repeated occurrences of data with references to a single copy of that data existing earlier in the uncompressed data stream. A match is encoded by a pair of numbers called a length-distance pair, which is equivalent to the statement "each of the next length characters is equal to the characters exactly distance characters behind it in the uncompressed stream". (The distance is sometimes called the offset instead.)

Asymmetric numeral systems

To spot matches, the encoder must keep track of some amount of the most recent data, such as the last 2 kB, 4 kB, or 32 kB. The structure in which this data is held is called a sliding window, which is why LZ77 is sometimes called sliding-window compression. The encoder needs to keep this data to look for matches, and the decoder needs to keep this data to interpret the matches the encoder refers to. The larger the sliding window is, the longer back the encoder may search for creating references.

It is not only acceptable but frequently useful to allow length-distance pairs to specify a length that actually exceeds the distance. As a copy command, this is puzzling: "Go back four characters and copy ten characters from that position into the current position". How can ten characters be copied over when only four of them are actually in the buffer? Tackling one byte at a time, there is no problem serving this request, because as a byte is copied over, it may be fed again as input to the copy command. When the copy-from position makes it to the initial destination position, it is consequently fed data that was pasted from the beginning of the copy-from position. The operation is thus equivalent to the statement "copy the data you were given and repetitively paste it until it fits". As this type of pair repeats a single copy of data multiple times, it can be used to incorporate a flexible and easy form of run-length encoding.

Another way to see things is as follows: While encoding, for the search pointer to continue finding matched pairs past the end of the search window, all characters from the first match at offset D and forward to the end of the search window must have matched input, and these are the (previously seen) characters that comprise a single run unit of length LR, which must equal D. Then as the search pointer proceeds past the search window and forward, as far as the run pattern repeats in the input, the search and input pointers will be in sync and match characters until the run pattern is interrupted. Then L characters have been matched in total, L > D, and the code is [D, L, c].

Upon decoding [D, L, c], again, D = LR. When the first LR characters are read to the output, this corresponds to a single run unit appended to the output buffer. At this point, the read pointer could be thought of as only needing to return int(L/LR) + (1 if L mod LR ≠ 0) times to the start of that single buffered run unit, read LR characters (or maybe fewer on the last return), and repeat until a total of L characters are read. But mirroring the encoding process, since the pattern is repetitive, the read pointer need only trail in sync with the write pointer by a fixed distance equal to the run length LR until L characters have been copied to output in total.

Considering the above, especially if the compression of data runs is expected to predominate, the window search should begin at the end of the window and proceed backwards, since run patterns, if they exist, will be found first and allow the search to terminate, absolutely if the current maximal matching sequence length is met, or judiciously, if a sufficient length is met, and finally for the simple possibility that the data is more recent and may correlate better with the next input.

LZ77 algorithms achieve compression by replacing repeated occurrences of data with references to a single copy of that data existing earlier in the uncompressed data stream. A match is encoded by a pair of numbers called a length-distance pair, which is equivalent to the statement "each of the next length characters is equal to the characters exactly distance characters behind it in the uncompressed stream". (The distance is sometimes called the offset instead.)

To spot matches, the encoder must keep track of some amount of the most recent data, such as the last 2 kB, 4 kB, or 32 kB. The structure in which this data is held is called a sliding window, which is why LZ77 is sometimes called sliding-window compression. The encoder needs to keep this data to look for matches, and the decoder needs to keep this data to interpret the matches the encoder refers to. The larger the sliding window is, the longer back the encoder may search for creating references.

It is not only acceptable but frequently useful to allow length-distance pairs to specify a length that actually exceeds the distance. As a copy command, this is puzzling: "Go back four characters and copy ten characters from that position into the current position". How can ten characters be copied over when only four of them are actually in the buffer? Tackling one byte at a time, there is no problem serving this request, because as a byte is copied over, it may be fed again as input to the copy command. When the copy-from position makes it to the initial destination position, it is consequently fed data that was pasted from the beginning of the copy-from position. The operation is thus equivalent to the statement "copy the data you were given and repetitively paste it until it fits". As this type of pair repeats a single copy of data multiple times, it can be used to incorporate a flexible and easy form of run-length encoding.

This way let to see things is as follows: While encoding, for the search pointer to continue finding matched pairs past the end of the search window, all characters from the first match at offset D and forward to the end of the search window must have matched input, and these are the (previously seen) characters that comprise a single run unit of length LR, which must equal D. Then as the search pointer proceeds past the search window and forward, as far as the run pattern repeats in the input, the search and input pointers will be in sync and match characters until the run pattern is interrupted. Then L characters have been matched in total, L > D, and the code is [D, L, c].

Upon decoding [D, L, c], again, D = LR. When the first LR characters are read to the output, this corresponds to a single run unit appended to the output buffer. At this point, the read pointer could be thought of as only needing to return int(L/LR) + (1 if L mod LR ≠ 0) times to the start of that single buffered run unit, read LR characters (or maybe fewer on the last return), and repeat until a total of L characters are read. But mirroring the encoding process, since the pattern is repetitive, the read pointer need only trail in sync with the write pointer by a fixed distance equal to the run length LR until L characters have been copied to output in total.

Considering the above, especially if the compression of data runs is expected to predominate, the window search should begin at the end of the window and proceed backwards, since run patterns, if they exist, will be found first and allow the search to terminate, absolutely if the current maximal matching sequence length is met, or judiciously, if a sufficient length is met, and finally for the simple possibility that the data is more recent and may correlate better with the next input.

In computer science and information theory, a Huffman code is a particular type of optimal prefix  that is commonly used for lossless data compression. The process of finding or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".

I have a patent who can pay for 5 000 000 euros.
Address: D11A3HA
We can meet at home.
