from html.parser import HTMLParser
from commapp.counter import Counter

class Zhk3HTMLParser(HTMLParser):

    curr_counter = Counter()
    counters = []
    tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append((tag, attrs))
        if tag == "td":
            if "class" in attrs[0]:
                if "meter-name" in attrs[0]:
                    self.curr_counter = Counter()


    def handle_endtag(self, tag):
        (open_tag, open_attrs) = self.tag_stack.pop()
        if tag == "a":
            (prev_tag, prev_attrs) = self.tag_stack[-1]
            if prev_tag == "td" and prev_attrs and "center meter-history" in prev_attrs[0]:
                self.curr_counter.info = open_attrs[0][1]
                self.curr_counter.id = open_attrs[0][1].split("=").pop()
        if tag == "td":
            assert tag == open_tag
            if "class" in open_attrs[0]:
                if "center meter-history" in open_attrs[0]:
                    self.counters.append(self.curr_counter)

    def handle_data(self, data):
        if self.tag_stack:
            (tag, attrs) = self.tag_stack[-1]
            if attrs and "class" in attrs[0]:
                if "meter-name" in attrs[0]:
                    self.curr_counter.name = data.replace(":","").strip()
                elif "cost" in attrs[0]:
                    if float(self.curr_counter.previous_value) < 0:
                        self.curr_counter.previous_value = data.strip()
                    else:
                        self.curr_counter.current_value = data.strip()

    def parse_text(self, text):
        parser = Zhk3HTMLParser()
        parser.feed(text)
        return parser.counters