import requests


class LeetCodeCrawler:
    def __init__(self):
        self.graphql_url = "https://leetcode.cn/graphql"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Content-Type': 'application/json',
            'Referer': 'https://leetcode.cn/problems/'
        }

    def get_problem_content(self, problem_slug):
        """获取题目内容"""
        query = """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                title
                titleSlug
                content
                difficulty
                translatedTitle
                translatedContent
                topicTags {
                    name
                    translatedName
                }
            }
        }
        """
        
        variables = {
            "titleSlug": problem_slug
        }
        
        response = requests.post(
            self.graphql_url,
            headers=self.headers,
            json={
                "query": query,
                "variables": variables
            }
        )
        
        try:
            data = response.json()
            if data and 'data' in data and 'question' in data['data']:
                return self._convert_to_markdown(data['data']['question'])
            else:
                print("API响应数据结构异常：", data)
                return None
        except Exception as e:
            print(f"处理响应时出错: {str(e)}")
            return None

    def _convert_to_markdown(self, question):
        """Convert problem data to Markdown format"""
        try:
            title_cn = question['translatedTitle']
            title_en = question['title']
            content = question['translatedContent']
            difficulty = question['difficulty']
            tags = question['topicTags']
            
            # Build Markdown
            markdown = f"# {title_cn}\n"
            markdown += f"难度：{difficulty}\n"
            
            # Add tags
            if tags:
                markdown += "标签: " + ", ".join([f"`{tag['name']}`" for tag in tags]) + "\n"
            
            markdown += "## Description\n"
            
            # Process HTML content
            content = content.replace('\n\n', '\n')  # Remove extra line breaks
            content = content.replace('<p>', '')     # Remove paragraph tags
            content = content.replace('</p>', '\n')  # Add line break after paragraphs
            content = content.replace('&nbsp;', '')  # Remove space characters
            content = content.replace('<ul>', '')    # Remove unordered list tags
            content = content.replace('</ul>', '')
            content = content.replace('<li>', '- ')  # Convert list items to markdown
            content = content.replace('</li>', '\n')
            content = content.replace('<pre>', '```\n')  # Convert code blocks
            content = content.replace('</pre>', '```\n')
            content = content.replace('<strong>', '**')  # Convert bold text
            content = content.replace('</strong>', '**')
            content = content.replace('<em>', '*')       # Convert italic text
            content = content.replace('</em>', '*')
            content = content.replace('<sup>', '^')      # Convert superscript
            content = content.replace('</sup>', '')
            
            # Clean up consecutive empty lines
            content = '\n'.join(line for line in content.splitlines() if line.strip())
            
            markdown += content + "\n"
            
            return markdown
        except Exception as e:
            print(f"Conversion error: {str(e)}")
            return None