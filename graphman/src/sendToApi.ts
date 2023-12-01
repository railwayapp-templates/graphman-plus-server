export async function sendToApi(json: any, apiEndpoint: string) {
    const response = await fetch(`https://${apiEndpoint}/upload`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(json),
    });
  
    if (!response.ok) {
      throw new Error(`Failed to send data to Flask: ${response.statusText}`);
    }
  
    return {message: "Success"}
  }